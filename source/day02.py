ID = "day-02"
TITLE = "Day 2: Ratios and Vocabulary"
KIND = "daily"
DATE = "Fri 6 Nov"
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
("Q","Ratios: difference","Teachers and students on a trip are in the ratio 3:8. There are 30 more students than teachers. How many people are on the trip?","66",["18","48","60"],"Extra boxes = 5. 5 boxes = 30, so 1 box = 6. Total boxes = 11. Total = 11 × 6 = 66.","30/5*11"),
("Q","Ratios: difference","Two numbers are in the ratio 2:5. When 12 is added to each, the ratio becomes 1:2. What is the larger original number?","60",["24","36","72"],"Gaps: 2:5 has gap 3, and 1:2 has gap 1. Change 1:2 to 3:6. Then 2 boxes become 3 boxes: +1 box = 12. Larger = 5 × 12 = 60. Check: 24 and 60 become 36 and 72, and 36:72 = 1:2.","5*12"),
("Q","Ratios: difference","Two numbers are in the ratio 6:11, and their difference is 40. What is the smaller number?","48",["40","56","88"],"Extra boxes = 5. 1 box = 8. Smaller = 6 × 8 = 48.","40/5*6"),
("Q","Ratios: linking","If A:B = 7:8 and B:C = 4:3, and C = 60, what is A?","70",["56","80","105"],"Make B equal to 8: B:C = 8:6. So A:B:C = 7:8:6. C is 6 boxes = 60, so 1 box = 10. A = 7 × 10 = 70.","60/6*7"),
("Q","Ratios: linking","If A:B = 1:2 and B:C = 4:3, and A + B + C = 810, what is B?","360",["180","270","450"],"Make B equal to 4: A:B = 2:4, so A:B:C = 2:4:3. Total boxes = 9. 1 box = 90. B = 4 × 90 = 360.","810/9*4"),
("Q","Ratios: linking","If A:B = 5:4 and B:C = 6:7, what is A:C?","15:14",["5:7","14:15","6:5"],"Make B equal to 12: A:B = 15:12 and B:C = 12:14. A:C = 15:14.",None),
("Q","Ratios: ages","The ages of two friends are in the ratio 5:6. In 7 years, the ratio will be 6:7. How old is the elder friend now?","42",["35","49","56"],"Both gaps are 1 box. +1 box = 7 years. Elder now = 6 × 7 = 42.","6*7"),
("Q","Ratios: ages","A father and son have ages in the ratio 8:3. In 15 years, the ratio will be 11:6. How old is the father now?","40",["15","45","55"],"Both gaps are 5 boxes. 8 boxes become 11 boxes: +3 boxes = 15 years, so 1 box = 5. Father now = 8 × 5 = 40. 55 is his age later.","8*5"),
("Q","Ratios: ages","The ages of two children are in the ratio 3:7. In 10 years, the ratio will be 2:3. How old is the elder child now?","14",["6","16","24"],"Gaps: 3:7 has gap 4, and 2:3 has gap 1. Change 2:3 to 8:12. Then 3 boxes become 8 boxes: +5 boxes = 10 years, so 1 box = 2. Elder now = 7 × 2 = 14.","7*2"),
("Q","Ratios: ages","The ages of two people are in the ratio 2:3, and the sum of their ages is 60. How old will the younger be in 5 years?","29",["24","36","41"],"Total boxes = 5. 1 box = 12. Younger now = 2 × 12 = 24. In 5 years = 29. 24 is the trap.","60/5*2+5"),
("Q","Ratios: ages","The present ages of two brothers are in the ratio 3:4. Six years ago, the ratio was 2:3. How old is the elder brother now?","24",["12","18","30"],"Both gaps are 1 box. Going back, 3 boxes become 2 boxes: −1 box = 6 years. Elder now = 4 × 6 = 24.","4*6"),
("Q","Ratios: ages","The ages of A and B are in the ratio 8:5, and A is 18 years older than B. How old was A five years ago?","43",["30","48","53"],"Extra boxes = 3. 1 box = 6. A now = 8 × 6 = 48. Five years ago = 43. 48 is the trap.","18/3*8-5"),
("Q","Ratios: general","The angles of a triangle are in the ratio 4:5:6. What is the smallest angle?","48°",["30°","60°","72°"],"Total boxes = 15. 1 box = 180 ÷ 15 = 12°. Smallest = 4 × 12 = 48°. 72° is the largest.","180/15*4"),
("Q","Ratios: general","The angles of a triangle are in the ratio 5:6:7. What is the middle angle?","60°",["50°","70°","90°"],"Total boxes = 18. 1 box = 10°. Middle = 6 × 10 = 60°.","180/18*6"),
("Q","Ratios: general","A jar holds Rs. 1 and Rs. 5 coins in the ratio 5:3. The total value is Rs. 100. How many Rs. 5 coins are there?","15",["3","5","25"],"One group = 5 Rs. 1 coins + 3 Rs. 5 coins = 5 + 15 = Rs. 20. Groups = 100 ÷ 20 = 5. Rs. 5 coins = 3 × 5 = 15. 5 is only the number of groups.","100/20*3"),
("Q","Ratios: general","A wallet holds Rs. 10 and Rs. 20 notes in the ratio 4:1. The total value is Rs. 600. How many Rs. 10 notes are there?","40",["10","20","30"],"One group = 4 Rs. 10 notes + 1 Rs. 20 note = 40 + 20 = Rs. 60. Groups = 600 ÷ 60 = 10. Rs. 10 notes = 4 × 10 = 40.","600/60*4"),
("Q","Ratios: general","A 30-litre mixture has milk and water in the ratio 7:3. How much water must be added to make the ratio 7:4?","3 litres",["2 litres","4 litres","6 litres"],"Total boxes = 10, so 1 box = 3. Milk = 21 and water = 9. Milk stays 21, so 1 box stays 3. New water = 4 × 3 = 12. Add 12 − 9 = 3 litres.","12-9"),
("Q","Ratios: general","Three partners share a profit of Rs. 84,000 in the ratio 1:2:4. What is the difference between the largest and smallest shares?","Rs. 36,000",["Rs. 12,000","Rs. 24,000","Rs. 48,000"],"Total boxes = 7. 1 box = 12,000. Difference = 4 − 1 = 3 boxes = 36,000.","84000/7*3"),
("Q","Ratios: general","If 15 pens cost Rs. 450, what will 8 pens cost?","Rs. 240",["Rs. 200","Rs. 300","Rs. 360"],"1 pen = 450 ÷ 15 = Rs. 30. 8 pens = 8 × 30 = 240.","450/15*8"),
("Q","Ratios: general","What is the simplest form of 0.6 : 0.9?","2:3",["1:2","3:2","3:4"],"Multiply both by 10: 6:9. Divide both by 3: 2:3.",None),
# Vocabulary: words missed earlier
("V","Synonyms","Choose the closest meaning of FASTIDIOUS.","Fussy about details",["Careless","Fast","Kind"],"Third test of this word. Picture someone wiping a clean plate three times before eating.",None),
("V","Synonyms","Choose the closest meaning of PUSILLANIMOUS.","Timid",["Courageous","Generous","Huge"],"Pusill = tiny, and anim = spirit. A tiny spirit means timid or cowardly.",None),
("V","Synonyms","Choose the closest meaning of VACILLATE.","Keep changing one's mind",["Reach a decision","Move quickly","Give an injection"],"Picture a person going back and forth between two choices.",None),
("V","Antonyms","Choose the opposite of AMELIORATE.","Make worse",["Make better","Soften","Delay"],"Melior = better. Ameliorate = make better, so \"make better\" is the synonym trap.",None),
("V","Antonyms","Choose the opposite of ACQUIESCE.","Object",["Consent","Comply","Rest"],"Acquiesce = quietly accept. Consent and comply are synonyms, so they are traps.",None),
("V","Antonyms","Choose the opposite of SANGUINE.","Gloomy",["Optimistic","Confident","Quiet"],"Sanguine = cheerfully hopeful. Optimistic and confident are synonyms, so they are traps.",None),
("V","Synonyms","Choose the closest meaning of VINDICATE.","Clear of blame",["Accuse","Punish","Ignore"],"Vindicate = prove someone right or innocent after doubt.",None),
("V","Synonyms","Choose the closest meaning of GRUDGING.","Unwilling",["Eager","Generous","Lavish"],"Grudging = given unwillingly.",None),
("V","Synonyms","Choose the closest meaning of MAGNANIMOUS.","Generous in forgiving",["Petty","Cowardly","Large in size"],"Magn = great, and anim = spirit. It describes a great spirit, not a large body.",None),
("V","Synonyms","Choose the closest meaning of CORROBORATE.","Confirm",["Deny","Collapse","Corrupt"],"Corroborate = support with evidence (تصدیق کرنا).",None),
# New words
("V","Synonyms","Choose the closest meaning of DEARTH.","Shortage",["Plenty","Death","Darkness"],"Dearth = a lack of something (قلت). It is not the same word as death.",None),
("V","Synonyms","Choose the closest meaning of CAJOLE.","Persuade by flattery",["Threaten","Punish","Trap"],"Cajole = persuade with gentle or flattering words (پھسلانا).",None),
("V","Antonyms","Choose the opposite of REDUNDANT.","Necessary",["Repeated","Excess","Unneeded"],"Redundant = no longer needed (زائد). The other three options are close in meaning.",None),
("V","Antonyms","Choose the opposite of TACIT.","Openly stated",["Unspoken","Silent","Polite"],"Tacit = understood without being said (خاموش). A tacit agreement is unspoken. Compare taciturn.",None),
# Tone and completion
("V","Critical reading","\"For all its grand language, the declaration commits no one to anything.\" The author's tone is:","critical",["admiring","joyful","fearful"],"\"For all its\" means \"despite\". The sentence ends on the failure: it commits no one to anything.",None),
("V","Critical reading","\"For all its flaws, the treaty remains the best hope for peace.\" The author's attitude is:","qualified support",["complete rejection","pure joy","deep fear"],"The same phrase can lead to a positive ending. The tone comes from what follows: \"the best hope for peace\".",None),
("V","Sentence completion","Her support was ______: she voted yes, but complained about it for a month.","reluctant",["eager","wholehearted","enthusiastic"],"The colon explains the blank. A yes followed by a month of complaints is reluctant.",None),
("V","Sentence completion","The accused, long thought ______, was finally ______ when new evidence proved his innocence.","guilty; vindicated",["innocent; condemned","guilty; condemned","innocent; accused"],"Start with the second blank: proof of innocence means vindicated. \"Long thought\" then needs a contrast: guilty.",None),
("V","Sentence completion","The committee ______ for weeks, unable to choose between the two plans.","vacillated",["decided","resolved","concluded"],"\"Unable to choose\" means going back and forth. The other options all mean reaching a decision.",None),
("V","Sentence completion","Instead of resisting, the workers ______ to the new rules without complaint.","acquiesced",["objected","rebelled","protested"],"\"Instead of resisting\" and \"without complaint\" both point to quiet acceptance.",None),
]
