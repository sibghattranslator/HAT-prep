ID = "verbal-01"
TITLE = "Verbal 1: Hard Vocabulary and Reading"
KIND = "daily"
DATE = "Fri 6 Nov"
MINUTES = 48

LESSON = """
<h3>Vocabulary: use the root</h3>
<pre>loqu = speak        loquacious = talkative
mal  = bad          malevolent = wishing harm
ben  = good         benevolent = kind
cred = believe      credulous = believes too easily
ver  = true         veracious = truthful
bell = war          bellicose = eager to fight
amb  = both         ambivalent = feeling both ways
in   = not          innocuous = not harmful</pre>

<h3>Antonym trap</h3>
<p>The options often include a synonym of the word. Decide the word's meaning first, then look for its <b>opposite</b>.</p>

<h3>Sentence completion</h3>
<p>Find the clue words before you read the options:</p>
<pre>although, but, yet, far from   = the idea changes
because, so, since             = the idea continues</pre>

<h3>Long passages</h3>
<pre>1. Read the first and last sentences. They often hold the main idea.
2. Read the rest and note the author's view.
3. Answer from the passage, not from your own knowledge.
4. Reject options with extreme words such as always, never, all.</pre>
"""

P1 = "The idea that states are equal and independent has shaped international law since at least the seventeenth century, yet it has always sat uneasily with the facts of power. In theory, a small island has the same legal sovereignty as a great power. In practice, the great power can shape the rules, ignore unfavourable judgments and reward those who follow its lead. Some scholars therefore dismiss international law as little more than politics in formal dress. This conclusion, however, is too hasty. Even powerful states spend considerable effort explaining why their actions are lawful, which would be strange if law did not matter. Moreover, most treaties are observed most of the time, largely because states expect to deal with one another again and value a reputation for keeping their word. The law's strength, then, lies less in any ability to punish than in the ordinary interests that make cooperation worthwhile. It does not remove power from world politics, but it does change the terms on which power is exercised."

P2 = "A common belief holds that translating a text is a matter of replacing each word with its equivalent in another language. Anyone who has tried it soon learns otherwise. Words carry histories, and a term that sounds neutral in one culture may be insulting or sacred in another. A legal phrase may have no counterpart at all, since the institution it names does not exist elsewhere. Translators must therefore decide what to preserve: the exact wording, the meaning, or the effect on the reader. These aims often conflict. A faithful version of a poem may lose its music, while a beautiful version may drift from the original. Machine translation has become remarkably useful for routine text, and many professionals now rely on it for first drafts. Yet the harder judgments remain human ones, at least for now, because they depend on knowing who will read the text and why. Translation, in short, is less a transfer of words than a series of choices."

def p(text, q):
    return {"p": text, "q": q}

Q = [
# Synonyms
("V","Synonyms","Choose the closest meaning of LOQUACIOUS.","Talkative",["Quiet","Wise","Brave"],"Root loqu = speak, as in eloquent. Loquacious = talkative (باتونی).",None),
("V","Synonyms","Choose the closest meaning of MALEVOLENT.","Wishing harm",["Generous","Tired","Cheerful"],"Root mal = bad, as in malice. Malevolent = wishing harm to others (بدخواہ).",None),
("V","Synonyms","Choose the closest meaning of CREDULOUS.","Believing too easily",["Doubtful","Dishonest","Famous"],"Root cred = believe, as in credit. A credulous person (خوش اعتقاد) is easily fooled.",None),
("V","Synonyms","Choose the closest meaning of AMBIVALENT.","Having mixed feelings",["Completely certain","Openly hostile","Often absent"],"Root amb = both. Ambivalent = pulled in both directions (متذبذب).",None),
("V","Synonyms","Choose the closest meaning of INTRANSIGENT.","Refusing to compromise",["Flexible","Temporary","Careless"],"In = not, and transigent comes from a root meaning to come to an agreement. Intransigent = refusing to agree or compromise (ہٹ دھرم).",None),
("V","Synonyms","Choose the closest meaning of EXACERBATE.","Make worse",["Ease","Explain","Delay"],"Exacerbate = make a bad situation worse. Root acer = sharp or bitter, as in acrimonious.",None),
("V","Synonyms","Choose the closest meaning of PERFUNCTORY.","Done with little care",["Thorough","Sudden","Highly skilled"],"Perfunctory = done quickly as a duty, without real care (سرسری).",None),
("V","Synonyms","Choose the closest meaning of SAGACIOUS.","Wise",["Foolish","Hungry","Bitter"],"Sagacious = wise and sound in judgment (دانا). A sage is a wise person.",None),
# Antonyms
("V","Antonyms","Choose the opposite of VERACIOUS.","Untruthful",["Honest","Greedy","Quick"],"Root ver = true, as in verify. Veracious = truthful. Do not confuse it with voracious, which means very hungry.",None),
("V","Antonyms","Choose the opposite of EQUIVOCAL.","Unambiguous",["Vague","Equal","Noisy"],"Equivocal = having two possible meanings (مبہم). Vague is a synonym, which is the trap.",None),
("V","Antonyms","Choose the opposite of PROFLIGATE.","Thrifty",["Wasteful","Proud","Early"],"Profligate = recklessly wasteful (فضول خرچ). The opposite is thrifty.",None),
("V","Antonyms","Choose the opposite of DILIGENT.","Lazy",["Hardworking","Polite","Careful"],"Diligent = hardworking and careful (محنتی). The opposite is lazy.",None),
("V","Antonyms","Choose the opposite of OSTENTATIOUS.","Modest",["Showy","Rich","Rude"],"Ostentatious = designed to impress or show off (نمائشی). The opposite is modest.",None),
("V","Antonyms","Choose the opposite of BELLICOSE.","Peaceable",["Aggressive","Beautiful","Ancient"],"Root bell = war, as in rebel. Bellicose = eager to fight (جنگجو). Do not confuse bell with belle, which means beautiful.",None),
("V","Antonyms","Choose the opposite of INNOCUOUS.","Harmful",["Harmless","Innocent","Small"],"In = not, and noc = harm. Innocuous = harmless, so the opposite is harmful.",None),
("V","Antonyms","Choose the opposite of EXTOL.","Condemn",["Praise","Remove","Extend"],"Extol = praise highly (تعریف کرنا). The opposite is condemn.",None),
# Completion
("V","Sentence completion","The diplomat's ______ reply neither confirmed nor denied the report.","equivocal",["candid","emphatic","hostile"],"\"Neither confirmed nor denied\" means the reply was unclear on purpose.",None),
("V","Sentence completion","Although the economy showed signs of recovery, analysts remained ______, warning that the gains could prove ______.","skeptical; temporary",["confident; lasting","delighted; permanent","indifferent; huge"],"\"Although\" changes the idea from recovery to doubt, and a warning needs a negative word such as temporary.",None),
("V","Sentence completion","The once ______ city, rich from trade, fell into ______ after the port closed.","prosperous; decline",["impoverished; decline","prosperous; growth","ruined; wealth"],"\"Rich from trade\" gives prosperous. \"Fell into\" and the port closing give decline.",None),
("V","Sentence completion","A judge must remain ______, favouring neither party.","impartial",["biased","partisan","anxious"],"\"Favouring neither party\" defines impartial (غیر جانبدار).",None),
("V","Sentence completion","His ______ manner made the negotiations harder, as he insulted every delegate.","abrasive",["tactful","gracious","timid"],"Insulting people is rough and harsh, which is abrasive (درشت).",None),
("V","Sentence completion","Far from ______ the dispute, the new statement only ______ it.","resolving; worsened",["worsening; resolved","causing; created","avoiding; settled"],"\"Far from\" sets up two opposite actions. The statement did not settle the dispute, and it made it worse.",None),
# Critical reading
("V","Critical reading","\"Exports rose after the country's currency fell, so a weaker currency always helps trade.\" What is the main flaw?","It generalises from a single case.",["It uses no numbers.","It discusses exports rather than imports.","It says the currency fell."],"One example cannot prove what \"always\" happens.",None),
("V","Critical reading","Most applicants who attended the workshop passed the test, and few who skipped it passed. Which statement is best supported?","Attending the workshop is linked with passing.",["The workshop guarantees a pass.","Everyone who attended passed.","Skipping makes passing impossible."],"\"Most\" and \"few\" support a link. They do not support guarantee, everyone or impossible.",None),
("V","Critical reading","Crime fell after a city hired more police, so the mayor says the hiring caused the fall. Which fact most weakens this claim?","Crime fell equally in nearby cities that hired no police.",["The new police officers were well trained.","Crime is a major concern for residents.","The city has a large police station."],"If crime fell equally without new police, something else may be the cause.",None),
("V","Critical reading","\"Although critics call the policy costly, it saves more than it spends, so it should continue.\" What is the author's conclusion?","The policy should continue.",["The policy is costly.","Critics are dishonest.","The policy saves money."],"\"So\" introduces the conclusion. \"It saves more than it spends\" is the reason.",None),
("V","Critical reading","\"The minister's so-called reform, announced with great fanfare, changed little beyond the name of the office.\" The author's tone is:","sarcastic",["admiring","joyful","fearful"],"\"So-called\" and \"changed little\" mock the gap between the big announcement and the small result.",None),
("V","Critical reading","\"The report was anything but clear.\" What does this sentence mean?","The report was unclear.",["The report was very clear.","The report covered everything.","Nothing could be clearer."],"\"Anything but\" means \"not at all\".",None),
# Passage 1
("V","Reading comprehension",p(P1,"What is the main idea of the passage?"),"International law does not remove power, but it still shapes how power is used.",["International law is only politics in formal dress.","All states obey international law because they fear punishment.","Small states have as much real power as great powers."],"The first option repeats the last sentence. The second is the view the author rejects.",None),
("V","Reading comprehension",p(P1,"How does the author view scholars who dismiss international law?"),"Their conclusion is too hasty.",["They are completely correct.","They are dishonest.","They have ignored the facts of power."],"The author says directly, \"This conclusion, however, is too hasty.\"",None),
("V","Reading comprehension",p(P1,"Why does the author mention powerful states explaining that their actions are lawful?"),"To show that law matters even to the powerful",["To prove that powerful states never break the law","To show that small states are equal in power","To criticise the seventeenth-century idea of law"],"The effort would be strange if law did not matter.",None),
("V","Reading comprehension",p(P1,"In this passage, \"sat uneasily with\" most nearly means:"),"was in tension with",["was comfortably supported by","was hidden from","was older than"],"Equality in theory conflicts with unequal power in practice.",None),
("V","Reading comprehension",p(P1,"According to the passage, why are most treaties observed?"),"States expect further dealings and value their reputation.",["Courts always punish states that break them.","Great powers force all states to obey.","Treaties are too difficult to break."],"This is stated in the sentence beginning \"Moreover\". The passage says the law's strength lies less in punishment.",None),
("V","Reading comprehension",p(P1,"With which statement would the author most likely agree?"),"A state may keep a treaty even when no one can punish it.",["Law matters only when it can punish.","Power has no role in world politics.","Small islands decide most international rules."],"The law's strength lies more in shared interests than in any ability to punish.",None),
# Passage 2
("V","Reading comprehension",p(P2,"What is the main idea of the passage?"),"Translation involves many choices, not just replacing words.",["Machines have replaced human translators.","Poems should never be translated.","Every word has an exact equivalent in another language."],"The last sentence states it directly. The first sentences reject the third wrong option.",None),
("V","Reading comprehension",p(P2,"Why may a legal phrase have no counterpart in another language?"),"The institution it names may not exist elsewhere.",["Legal phrases are always insulting.","Lawyers do not allow translation.","Machines cannot read legal text."],"This is stated in the fourth sentence.",None),
("V","Reading comprehension",p(P2,"What does the poem example show?"),"The aims of translation can conflict.",["Poems are easier to translate than laws.","Faithful versions are always the best.","Machine translation works best for poetry."],"It follows directly after \"These aims often conflict\": faithfulness and beauty can pull apart.",None),
("V","Reading comprehension",p(P2,"How does the author view machine translation?"),"Useful for routine text but limited for harder judgments",["Useless for professional work","Better than humans for all text","Dangerous and best avoided"],"The author calls it \"remarkably useful\" for routine text, but says the harder judgments remain human.",None),
("V","Reading comprehension",p(P2,"What does the phrase \"at least for now\" suggest?"),"This situation may change in the future.",["Machines will never improve.","Human translators are already gone.","The author is certain about the future."],"The phrase limits the claim to the present and leaves the future open.",None),
("V","Reading comprehension",p(P2,"Which is the best title for the passage?"),"Translation as a Series of Choices",["The History of Legal Language","Why Machines Translate Perfectly","How to Write a Poem"],"The title should cover the whole passage, and this one matches its final sentence.",None),
]
