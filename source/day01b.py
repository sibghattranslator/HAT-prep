ID = "day-01b"
TITLE = "Day 1 Retest: Ratios"
KIND = "daily"
DATE = "New numbers"
MINUTES = 48

LESSON = """
<h3>Before you start</h3>
<p>These are the same question types as Day 1, with new numbers and scenarios.</p>
<pre>1. Find one box.
2. Use the boxes the question needs.
3. Read the last line again: now or later? which person? one part or the total?</pre>
<p><b>Two facts to remember:</b> the angles of a triangle add up to 180°. When a question gives coins and a total value, find the value of one group first.</p>
"""

Q = [
# Difference
("Q","Ratios: difference","Two numbers are in the ratio 2:7, and their difference is 35. What is the larger number?","49",["14","42","56"],"Extra boxes = 5. 5 boxes = 35, so 1 box = 7. Larger = 7 × 7 = 49.","35/5*7"),
("Q","Ratios: difference","Two numbers are in the ratio 7:11, and their difference is 20. What is the larger number?","55",["35","45","60"],"Extra boxes = 4. 4 boxes = 20, so 1 box = 5. Larger = 11 × 5 = 55.","20/4*11"),
("Q","Ratios: difference","Two numbers are in the ratio 5:8, and their difference is 21. What is the smaller number?","35",["21","42","56"],"Extra boxes = 3. 3 boxes = 21, so 1 box = 7. Smaller = 5 × 7 = 35.","21/3*5"),
("Q","Ratios: difference","The salaries of X and Y are in the ratio 9:5. X earns Rs. 12,000 more than Y. What is Y's salary?","Rs. 15,000",["Rs. 12,000","Rs. 18,000","Rs. 27,000"],"Extra boxes = 4. 4 boxes = 12,000, so 1 box = 3,000. Y = 5 × 3,000 = 15,000.","12000/4*5"),
("Q","Ratios: difference","Apples and oranges in a shop are in the ratio 9:4. There are 30 more apples than oranges. How many pieces of fruit are there in total?","78",["24","54","72"],"Extra boxes = 5. 5 boxes = 30, so 1 box = 6. Total boxes = 13. Total = 13 × 6 = 78.","30/5*13"),
("Q","Ratios: difference","Two numbers are in the ratio 4:9, and their difference is 25. What is their sum?","65",["20","45","60"],"Extra boxes = 5. 5 boxes = 25, so 1 box = 5. Sum = 13 boxes = 13 × 5 = 65.","25/5*13"),
("Q","Ratios: difference","Two numbers are in the ratio 1:3. When 10 is added to each, the ratio becomes 1:2. What is the larger original number?","30",["10","20","40"],"Gaps: 1:3 has gap 2, and 1:2 has gap 1. Change 1:2 to 2:4 so the gap is 2. Then 1 box becomes 2 boxes: +1 box = 10. Larger = 3 × 10 = 30. Check: 10 and 30 become 20 and 40, and 20:40 = 1:2.","10*3"),
# Linking
("Q","Ratios: linking","If A:B = 3:4 and B:C = 4:5, what is A:C?","3:5",["3:4","4:5","5:3"],"B is 4 in both, so A:B:C = 3:4:5. A:C = 3:5.",None),
("Q","Ratios: linking","If P:Q = 1:3 and Q:R = 3:7, what is P:R?","1:7",["1:3","3:7","7:1"],"Q is 3 in both, so P:Q:R = 1:3:7. P:R = 1:7.",None),
("Q","Ratios: linking","If A:B = 3:4 and B:C = 5:9, what is A:C?","5:12",["1:3","4:5","12:5"],"Make B equal to 20: A:B = 15:20 and B:C = 20:36. A:C = 15:36. Divide both by 3: 5:12.",None),
("Q","Ratios: linking","If A:B = 5:6 and B:C = 9:4, what is A:C?","15:8",["8:15","5:4","3:2"],"Make B equal to 18: A:B = 15:18 and B:C = 18:8. A:C = 15:8.",None),
("Q","Ratios: linking","If A:B = 3:5 and B:C = 3:4, what is A:B:C?","9:15:20",["3:5:4","9:5:4","3:15:20"],"Make B equal to 15: A:B = 9:15 and B:C = 15:20. A:B:C = 9:15:20.",None),
("Q","Ratios: linking","If A:B = 3:2 and B:C = 4:5, and A + B + C = 600, what is C?","200",["160","240","300"],"Make B equal to 4: A:B = 6:4, so A:B:C = 6:4:5. Total boxes = 15. 1 box = 40. C = 5 × 40 = 200.","600/15*5"),
("Q","Ratios: linking","If A:B = 4:9 and B:C = 3:2, and C = 30, what is A?","20",["15","30","45"],"Make B equal to 9: B:C = 3:2 × 3 = 9:6. So A:B:C = 4:9:6. C is 6 boxes = 30, so 1 box = 5. A = 4 × 5 = 20.","30/6*4"),
# Ages
("Q","Ratios: ages","The ages of two friends are in the ratio 4:5. In 6 years, the ratio will be 5:6. How old is the elder friend now?","30",["24","36","42"],"Both gaps are 1 box. 4 boxes become 5 boxes: +1 box = 6 years. Elder now = 5 × 6 = 30.","5*6"),
("Q","Ratios: ages","The ages of two brothers are in the ratio 5:6. In 3 years, the ratio will be 6:7. How old is the elder brother now?","18",["15","21","24"],"Both gaps are 1 box. +1 box = 3 years. Elder now = 6 × 3 = 18.","6*3"),
("Q","Ratios: ages","The ages of two colleagues are in the ratio 3:5. In 8 years, the ratio will be 2:3. How old is the younger colleague now?","24",["16","32","40"],"Gaps: 3:5 has gap 2, and 2:3 has gap 1. Change 2:3 to 4:6. Then 3 boxes become 4 boxes: +1 box = 8 years. Younger now = 3 × 8 = 24.","3*8"),
("Q","Ratios: ages","A mother and daughter have ages in the ratio 9:2. In 8 years, the ratio will be 11:4. How old is the mother now?","36",["8","40","44"],"Both gaps are 7 boxes. 9 boxes become 11 boxes: +2 boxes = 8 years, so 1 box = 4. Mother now = 9 × 4 = 36.","9*4"),
("Q","Ratios: ages","The present ages of two sisters are in the ratio 4:5. Six years ago, the ratio was 3:4. How old is the younger sister now?","24",["18","30","36"],"Both gaps are 1 box. Going back, 4 boxes become 3 boxes: −1 box = 6 years. Younger now = 4 × 6 = 24.","4*6"),
("Q","Ratios: ages","The ages of two people are in the ratio 5:7, and the sum of their ages is 72. How old will the elder be in 8 years?","50",["38","42","58"],"Total boxes = 12. 1 box = 6. Elder now = 7 × 6 = 42. In 8 years = 50. The question asks about 8 years from now, so 42 is the trap.","72/12*7+8"),
("Q","Ratios: ages","The ages of A and B are in the ratio 7:4, and A is 15 years older than B. How old will B be in 6 years?","26",["20","35","41"],"Extra boxes = 3. 1 box = 5. B now = 4 × 5 = 20. In 6 years = 26.","15/3*4+6"),
# General
("Q","Ratios: general","What is the simplest form of 0.25 : 0.75?","1:3",["1:2","2:3","3:4"],"Multiply both by 100: 25:75. Divide both by 25: 1:3.",None),
("Q","Ratios: general","A 60-litre mixture has milk and water in the ratio 2:1. How much water must be added to make the ratio 4:3?","10 litres",["5 litres","20 litres","30 litres"],"Milk = 40 and water = 20. Milk stays 40. For 4:3, 4 boxes = 40, so 1 box = 10 and water must be 30. Add 30 − 20 = 10 litres.","30-20"),
("Q","Ratios: general","Three partners share a profit of Rs. 90,000 in the ratio 1:3:5. What is the difference between the largest and smallest shares?","Rs. 40,000",["Rs. 10,000","Rs. 30,000","Rs. 50,000"],"Total boxes = 9. 1 box = 10,000. Difference = 5 − 1 = 4 boxes = 40,000.","90000/9*4"),
("Q","Ratios: general","If 8 kg of rice costs Rs. 640, what will 15 kg cost?","Rs. 1,200",["Rs. 960","Rs. 1,000","Rs. 1,280"],"1 kg = 640 ÷ 8 = Rs. 80. 15 kg = 15 × 80 = 1,200.","640/8*15"),
("Q","Ratios: general","The angles of a triangle are in the ratio 3:4:5. What is the largest angle?","75°",["45°","60°","90°"],"Angles of a triangle add up to 180°. Total boxes = 12. 1 box = 15°. Largest = 5 × 15 = 75°.","180/12*5"),
("Q","Ratios: general","A bag holds Rs. 2 and Rs. 5 coins in the ratio 5:2. The total value is Rs. 200. How many Rs. 5 coins are there?","20",["10","40","50"],"One group = 5 Rs. 2 coins + 2 Rs. 5 coins = 10 + 10 = Rs. 20. Groups = 200 ÷ 20 = 10. Rs. 5 coins = 2 × 10 = 20.","200/20*2"),
# Analytical
("A","Conditional logic","If the gate is locked, the guard has left. The guard has not left. What can we conclude?","The gate is not locked.",["The gate is locked.","The guard will leave later.","Nothing can be concluded."],"If P then Q. Not Q, so not P.",None),
("A","Conditional logic","If it rains, the road gets wet. The road is wet. What can we conclude?","Nothing certain about the rain.",["It rained.","It did not rain.","It will rain tomorrow."],"You cannot go backward from Q to P. The road could be wet for another reason.",None),
("A","Conditional logic","Only licensed drivers may rent a car. Bilal rented a car. What must be true?","Bilal is a licensed driver.",["All licensed drivers rent cars.","Bilal has no licence.","Nothing can be concluded."],"\"Only licensed drivers may rent\" means: if you rented, you are licensed.",None),
("A","Ordering","Sara is older than Hina but younger than Amna. Zoya is younger than Hina. Who is the second youngest?","Hina",["Amna","Sara","Zoya"],"Oldest first: Amna > Sara > Hina > Zoya. Second from the young end is Hina.",None),
("A","Ordering","Tariq finished after Usman but before Wasim. Yasir finished after Wasim but before Zahid. Who finished third?","Wasim",["Tariq","Yasir","Usman"],"The order is Usman, Tariq, Wasim, Yasir, Zahid. Third is Wasim.",None),
("A","Series","What comes next? 3, 8, 15, 24, 35, ?","48",["44","46","50"],"The gaps are 5, 7, 9, 11, then 13. 35 + 13 = 48.","35+13"),
("A","Coding","If PLANT is coded as QMBOU, how is STONE coded?","TUPOF",["TUPOE","RSNMD","TUONF"],"Each letter moves one forward: S→T, T→U, O→P, N→O, E→F.",None),
# Verbal
("V","Synonyms","Choose the closest meaning of MUNDANE.","Ordinary",["Strange","Sacred","Hostile"],"Mundane = ordinary and dull (معمولی).",None),
("V","Antonyms","Choose the opposite of GREGARIOUS.","Unsociable",["Friendly","Outgoing","Greedy"],"Gregarious = fond of company (ملنسار). Root: grex, \"flock\". The opposite is unsociable.",None),
("V","Analogies","HUMBLE : BOAST. Choose the pair with the same relationship.","Honest : Lie",["Angry : Shout","Thirsty : Drink","Student : Read"],"A humble person does not boast. An honest person does not lie.",None),
("V","Sentence completion","Far from being ______, her report was carefully researched and ______ every claim with evidence.","careless; supported",["thorough; supported","meticulous; questioned","rigorous; backed"],"\"Far from\" needs the opposite of \"carefully researched\", which is careless. The second blank needs supported.",None),
("V","Grammar","Neither of the reports ______ been approved.","has",["have","are","were"],"\"Neither\" is singular, so it takes \"has\". Ignore the phrase \"of the reports\".",None),
("V","Error spotting","Which part contains an error? \"The minister has signed the agreement, and its terms is now public.\"","its terms is",["has signed","the agreement","now public"],"\"Terms\" is plural, so it should be \"its terms are\". The word \"its\" does not make the subject singular.",None),
]
