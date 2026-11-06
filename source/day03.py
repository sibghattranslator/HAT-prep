ID = "day-03"
TITLE = "Day 3: Ratios and Vocabulary"
KIND = "daily"
DATE = "Sat 7 Nov"
MINUTES = 48

LESSON = """
<h3>Before you start</h3>
<pre>Ratios:   after you find a number, read the last line again.
Antonyms: cross out any option that means the same as the word.
Tone:     "for all its X" means "despite X". The tone comes from what follows.
Colon:    the words after a colon explain the blank.</pre>
<p>Use about 60 to 70 seconds a question, and click <b>Mark as unsure</b> when you guess.</p>
"""

Q = [
# Ratios
("Q","Ratios: difference","Buses and cars in a car park are in the ratio 2:9. There are 42 more cars than buses. How many vehicles are there in total?","66",["12","54","77"],"Extra boxes = 7. 7 boxes = 42, so 1 box = 6. Total boxes = 11. Total = 11 × 6 = 66.","42/7*11"),
("Q","Ratios: difference","Two numbers are in the ratio 3:7. When 8 is added to each, the ratio becomes 1:2. What is the larger original number?","56",["24","32","64"],"Gaps: 3:7 has gap 4, and 1:2 has gap 1. Change 1:2 to 4:8. Then 3 boxes become 4 boxes: +1 box = 8. Larger = 7 × 8 = 56. Check: 24 and 56 become 32 and 64, and 32:64 = 1:2.","7*8"),
("Q","Ratios: difference","Two numbers are in the ratio 7:12, and their difference is 35. What is the smaller number?","49",["35","70","84"],"Extra boxes = 5. 1 box = 7. Smaller = 7 × 7 = 49.","35/5*7"),
("Q","Ratios: linking","If A:B = 2:5 and B:C = 3:4, and C = 80, what is A?","24",["30","40","60"],"Make B equal to 15: A:B = 6:15 and B:C = 15:20. So A:B:C = 6:15:20. C is 20 boxes = 80, so 1 box = 4. A = 6 × 4 = 24.","80/20*6"),
("Q","Ratios: linking","If A:B = 3:4 and B:C = 2:5, and A + B + C = 340, what is C?","200",["60","80","300"],"Make B equal to 4: B:C = 4:10, so A:B:C = 3:4:10. Total boxes = 17. 1 box = 340 ÷ 17 = 20. C = 10 × 20 = 200.","340/17*10"),
("Q","Ratios: linking","If A:B = 4:3 and B:C = 9:2, what is A:C?","6:1",["4:2","2:1","12:2"],"Make B equal to 9: A:B = 12:9 and B:C = 9:2. A:C = 12:2 = 6:1.",None),
("Q","Ratios: ages","The ages of two brothers are in the ratio 6:7. In 4 years, the ratio will be 7:8. How old is the elder brother now?","28",["24","32","35"],"Both gaps are 1 box. +1 box = 4 years. Elder now = 7 × 4 = 28. 32 is his age later.","7*4"),
("Q","Ratios: ages","A mother and son have ages in the ratio 9:4. In 6 years, the ratio will be 11:6. How old is the mother now?","27",["12","33","36"],"Both gaps are 5 boxes. 9 boxes become 11 boxes: +2 boxes = 6 years, so 1 box = 3. Mother now = 9 × 3 = 27. 33 is her age later.","9*3"),
("Q","Ratios: ages","The ages of two cousins are in the ratio 2:5. In 9 years, the ratio will be 1:2. How old is the elder cousin now?","45",["18","27","54"],"Gaps: 2:5 has gap 3, and 1:2 has gap 1. Change 1:2 to 3:6. Then 2 boxes become 3 boxes: +1 box = 9 years. Elder now = 5 × 9 = 45. Check: 18 and 45 become 27 and 54, and 27:54 = 1:2.","5*9"),
("Q","Ratios: ages","The ages of two people are in the ratio 3:5, and the sum of their ages is 64. How old will the elder be in 4 years?","44",["24","40","48"],"Total boxes = 8. 1 box = 8. Elder now = 5 × 8 = 40. In 4 years = 44. 40 is the trap.","64/8*5+4"),
("Q","Ratios: ages","The present ages of two sisters are in the ratio 5:6. Four years ago, the ratio was 4:5. How old is the younger sister now?","20",["16","24","28"],"Both gaps are 1 box. Going back, 5 boxes become 4 boxes: −1 box = 4 years. Younger now = 5 × 4 = 20.","5*4"),
("Q","Ratios: ages","The ages of A and B are in the ratio 9:4, and A is 25 years older than B. How old was B three years ago?","17",["20","42","45"],"Extra boxes = 5. 1 box = 5. B now = 4 × 5 = 20. Three years ago = 17. 20 is the trap.","25/5*4-3"),
("Q","Ratios: general","The angles of a triangle are in the ratio 1:2:3. What is the largest angle?","90°",["30°","60°","120°"],"Total boxes = 6. 1 box = 180 ÷ 6 = 30°. Largest = 3 × 30 = 90°.","180/6*3"),
("Q","Ratios: general","The angles of a triangle are in the ratio 2:5:8. What is the smallest angle?","24°",["36°","60°","96°"],"Total boxes = 15. 1 box = 12°. Smallest = 2 × 12 = 24°. 96° is the largest.","180/15*2"),
("Q","Ratios: general","A purse holds Rs. 2 and Rs. 10 coins in the ratio 4:1. The total value is Rs. 180. How many Rs. 2 coins are there?","40",["10","18","50"],"One group = 4 Rs. 2 coins + 1 Rs. 10 coin = 8 + 10 = Rs. 18. Groups = 180 ÷ 18 = 10. Rs. 2 coins = 4 × 10 = 40. 10 is only the number of groups.","180/18*4"),
("Q","Ratios: general","A drawer holds Rs. 50 and Rs. 100 notes in the ratio 3:2. The total value is Rs. 1,400. How many Rs. 100 notes are there?","8",["4","12","20"],"One group = 3 Rs. 50 notes + 2 Rs. 100 notes = 150 + 200 = Rs. 350. Groups = 1,400 ÷ 350 = 4. Rs. 100 notes = 2 × 4 = 8.","1400/350*2"),
("Q","Ratios: general","A 50-litre mixture has milk and water in the ratio 4:1. How much water must be added to make the ratio 2:1?","10 litres",["5 litres","15 litres","20 litres"],"Total boxes = 5, so 1 box = 10. Milk = 40 and water = 10. Milk stays 40. For 2:1, water must be 20. Add 20 − 10 = 10 litres.","20-10"),
("Q","Ratios: general","Three partners share Rs. 1,20,000 in the ratio 2:3:5. What is the difference between the largest and smallest shares?","Rs. 36,000",["Rs. 12,000","Rs. 24,000","Rs. 60,000"],"Total boxes = 10. 1 box = 12,000. Difference = 5 − 2 = 3 boxes = 36,000.","120000/10*3"),
("Q","Ratios: general","If 6 metres of cloth cost Rs. 900, what will 10 metres cost?","Rs. 1,500",["Rs. 1,200","Rs. 1,350","Rs. 1,800"],"1 metre = 900 ÷ 6 = Rs. 150. 10 metres = 10 × 150 = 1,500.","900/6*10"),
("Q","Ratios: general","What is the simplest form of 1.2 : 1.8?","2:3",["1:2","3:2","4:5"],"Multiply both by 10: 12:18. Divide both by 6: 2:3.",None),
# Vocabulary
("V","Synonyms","Choose the closest meaning of FASTIDIOUS.","Demanding about details",["Relaxed","Speedy","Friendly"],"Fourth test of this word. A fastidious person is very hard to please about small details.",None),
("V","Synonyms","Choose the closest meaning of PUSILLANIMOUS.","Lacking courage",["Bold","Kind-hearted","Tiny in size"],"Pusill = tiny, and anim = spirit. A tiny spirit, not a tiny body.",None),
("V","Antonyms","Choose the opposite of VACILLATE.","Stand firm",["Waver","Hesitate","Swing"],"Vacillate = keep changing one's mind. Waver, hesitate and swing are close in meaning, so they are traps.",None),
("V","Antonyms","Choose the opposite of AMELIORATE.","Aggravate",["Improve","Ease","Relieve"],"Ameliorate = make better. Improve, ease and relieve are synonyms. Aggravate = make worse.",None),
("V","Synonyms","Choose the closest meaning of ACQUIESCE.","Accept quietly",["Protest","Acquire","Question"],"Acquiesce = accept without protest. Remember quies, the root of \"quiet\".",None),
("V","Synonyms","Choose the closest meaning of SANGUINE.","Hopeful",["Gloomy","Bloody","Angry"],"Sanguine = cheerfully hopeful (پرامید).",None),
("V","Antonyms","Choose the opposite of VINDICATE.","Incriminate",["Justify","Clear","Defend"],"Vindicate = clear of blame. Incriminate = make someone appear guilty.",None),
("V","Antonyms","Choose the opposite of GRUDGING.","Wholehearted",["Reluctant","Unwilling","Bitter"],"Grudging = given unwillingly. Reluctant and unwilling are synonyms, so they are traps.",None),
("V","Synonyms","Choose the closest meaning of DEARTH.","Scarcity",["Abundance","Death","Distance"],"Dearth = a lack of something (قلت).",None),
("V","Antonyms","Choose the opposite of TACIT.","Explicit",["Implied","Silent","Unspoken"],"Tacit = understood without being said. Explicit = clearly stated.",None),
# New words
("V","Synonyms","Choose the closest meaning of DILATORY.","Slow to act",["Prompt","Wide","Painful"],"Dilatory = tending to delay (سست). Do not confuse it with dilate, which means widen.",None),
("V","Synonyms","Choose the closest meaning of IMPECCABLE.","Flawless",["Careless","Impossible","Rough"],"In = not, and pecc = sin or fault. Impeccable = without any fault (بے عیب).",None),
("V","Antonyms","Choose the opposite of PAROCHIAL.","Broad-minded",["Narrow","Local","Religious"],"Parochial = having a narrow, local outlook (تنگ نظر). Narrow and local are traps.",None),
("V","Antonyms","Choose the opposite of CANDOUR.","Deceit",["Honesty","Frankness","Sweetness"],"Candour = honesty and openness. You saw candid in your first test.",None),
# Tone and completion
("V","Critical reading","\"For all its expensive equipment, the hospital still turns patients away.\" The author's tone is:","critical",["admiring","joyful","relieved"],"\"For all its\" means \"despite\". The sentence ends on the failure: it still turns patients away.",None),
("V","Critical reading","\"For all its noise and crowds, the old bazaar remains the heart of the city.\" The author's attitude is:","affectionate",["disgusted","fearful","indifferent"],"The sentence ends on a warm point: \"the heart of the city\".",None),
("V","Sentence completion","His apology was ______: he said sorry, then blamed everyone else.","half-hearted",["sincere","heartfelt","complete"],"The colon explains the blank. An apology followed by blaming others is not sincere.",None),
("V","Sentence completion","Once ______ as reckless, the minister was ______ when his policy saved the economy.","dismissed; vindicated",["praised; condemned","admired; criticised","dismissed; blamed"],"Start with the second blank: saving the economy proves him right, so vindicated. \"Once\" then needs a contrast: dismissed.",None),
("V","Sentence completion","Instead of deciding quickly, the board ______ for months.","dithered",["resolved","acted","settled"],"\"Instead of deciding quickly\" means hesitating. Dither = be unable to decide, like vacillate.",None),
("V","Sentence completion","The officer was ______ in his duties, never leaving a file late or incomplete.","punctilious",["dilatory","negligent","careless"],"Punctilious = very careful about rules and details. Dilatory means the opposite.",None),
]
