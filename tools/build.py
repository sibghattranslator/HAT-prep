"""Checks every source paper and writes papers/*.js. Run: python tools/build.py"""
import glob, importlib.util, json, os, random, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECT = {"mock": {"V": 40, "A": 35, "Q": 25}}
errors, ids = [], []


def num(text):
    m = re.match(r"^(?:Rs\. )?(−?[\d,]+(?:\.\d+)?)", text)
    return float(m.group(1).replace(",", "").replace("−", "-")) if m else None


os.makedirs(os.path.join(ROOT, "papers"), exist_ok=True)
for path in sorted(glob.glob(os.path.join(ROOT, "source", "*.py"))):
    spec = importlib.util.spec_from_file_location("paper", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    rng = random.Random(m.ID)
    out, counts = [], {"V": 0, "A": 0, "Q": 0}
    for i, (sec, topic, q, ans, wrong, expl, check) in enumerate(m.Q, 1):
        counts[sec] += 1
        where = f"{m.ID} Q{i}"
        passage, text = (q["p"], q["q"]) if isinstance(q, dict) else ("", q)
        opts = [ans] + wrong
        if len(opts) != 4 or len(set(opts)) != 4:
            errors.append(f"{where}: needs 4 different options")
        if check is not None:
            value = eval(check, {})
            if num(ans) is None or abs(value - num(ans)) > 1e-9:
                errors.append(f"{where}: key {ans} but check gives {value}")
        if sec == "Q" and check is None and not re.search(r"\d+[:/]\d+|decrease", ans):
            errors.append(f"{where}: quantitative answer has no check")
        if all(num(o) is not None for o in opts):
            opts.sort(key=num)
        else:
            rng.shuffle(opts)
        out.append({"s": sec, "t": topic, "p": passage, "q": text, "o": opts,
                    "a": opts.index(ans), "e": expl})
    want = EXPECT.get(m.KIND)
    if want and counts != want:
        errors.append(f"{m.ID}: section counts {counts}, expected {want}")
    paper = {"id": m.ID, "title": m.TITLE, "kind": m.KIND, "date": m.DATE,
             "minutes": m.MINUTES, "lesson": m.LESSON, "questions": out}
    with open(os.path.join(ROOT, "papers", m.ID + ".js"), "w", encoding="utf-8") as f:
        f.write("HAT_PAPERS.push(" + json.dumps(paper, ensure_ascii=False) + ");\n")
    ids.append(m.ID)
    print(m.ID, len(out), counts)

with open(os.path.join(ROOT, "papers", "list.js"), "w", encoding="utf-8") as f:
    f.write("var HAT_PAPERS = [];\nvar HAT_LIST = " + json.dumps(ids) + ";\n")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("All checks passed")
