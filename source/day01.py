ID = "day-01"
TITLE = "Day 1: Ratios"
KIND = "daily"
DATE = "Fri 6 Nov"
MINUTES = 48

LESSON = """
<h3>The one idea: boxes</h3>
<p>A ratio (تناسب) of 3:5 means 3 equal boxes and 5 equal boxes. Find what <b>one box</b> is worth, then multiply.</p>

<h3>Trick 1: the difference is given</h3>
<p><b>Two numbers are in the ratio 2:5, and their difference is 30. Find the larger.</b></p>
<pre>Small:  [ ][ ]
Large:  [ ][ ][ ][ ][ ]
Extra boxes = 5 − 2 = 3
3 boxes = 30, so 1 box = 10
Large = 5 × 10 = 50</pre>

<h3>Trick 2: linking two ratios</h3>
<p>To join A:B and B:C, B must be the <b>same number</b> in both.</p>
<p><b>A:B = 2:3 and B:C = 5:7. Find A:C.</b></p>
<pre>B is 3 and 5. Make both 15.
A:B = 2:3  (× 5) = 10:15
B:C = 5:7  (× 3) = 15:21
A:B:C = 10:15:21, so A:C = 10:21</pre>

<h3>Trick 3: age questions</h3>
<p>Every year, both people get older by the <b>same number</b>. So the gap between their ages never changes.</p>
<p><b>Two brothers are in the ratio 3:4. In 5 years, the ratio will be 4:5. How old is the elder now?</b></p>
<pre>Now:     3 : 4   (gap = 1 box)
Later:   4 : 5   (gap = 1 box)
The gaps match, so the boxes are the same size.
Younger goes from 3 boxes to 4 boxes: +1 box
5 years = 1 box
Elder now = 4 × 5 = 20
Check: 15 and 20 now, 20 and 25 later. 20:25 = 4:5 ✓</pre>
<p><b>If the gaps do not match</b>, multiply a ratio until they do. For 5:7 now (gap 2) and 3:4 later (gap 1), change 3:4 to 6:8 (gap 2). Then 5 boxes become 6 boxes.</p>
<p>Always read the last line of the question: is it asking for the younger or elder, now or later?</p>
"""

Q = [
# Difference
("Q","Ratios: difference","Two numbers are in the ratio 3:7, and their difference is 20. What is the larger number?","35",["15","28","50"],"Extra boxes = 7 − 3 = 4. 4 boxes = 20, so 1 box = 5. Larger = 7 × 5 = 35.","20/4*7"),
("Q","Ratios: difference","Two numbers are in the ratio 5:9, and their difference is 32. What is the larger number?","72",["40","56","63"],"Extra boxes = 4. 4 boxes = 32, so 1 box = 8. Larger = 9 × 8 = 72.","32/4*9"),
("Q","Ratios: difference","Two numbers are in the ratio 4:7, and their difference is 27. What is the smaller number?","36",["27","45","63"],"Extra boxes = 3. 3 boxes = 27, so 1 box = 9. Smaller = 4 × 9 = 36. Note that the question asks for the smaller number.","27/3*4"),
("Q","Ratios: difference","The incomes of A and B are in the ratio 7:4. A earns Rs. 15,000 more than B. What is B's income?","Rs. 20,000",["Rs. 15,000","Rs. 25,000","Rs. 35,000"],"Extra boxes = 3. 3 boxes = 15,000, so 1 box = 5,000. B = 4 × 5,000 = 20,000.","15000/3*4"),
("Q","Ratios: difference","Men and women at a meeting are in the ratio 8:5. There are 24 more men than women. How many people are there in total?","104",["40","64","96"],"Extra boxes = 3. 3 boxes = 24, so 1 box = 8. Total boxes = 8 + 5 = 13. Total people = 13 × 8 = 104.","24/3*13"),
("Q","Ratios: difference","Two numbers are in the ratio 5:8, and their difference is 12. What is their sum?","52",["20","32","48"],"Extra boxes = 3. 3 boxes = 12, so 1 box = 4. Sum = 13 boxes = 13 × 4 = 52.","12/3*13"),
("Q","Ratios: difference","Two numbers are in the ratio 3:5. When 9 is added to each, the ratio becomes 3:4. What is the larger original number?","15",["9","18","24"],"The gaps differ: 3:5 has gap 2, and 3:4 has gap 1. Change 3:4 to 6:8 so the gap is 2. Then 3 boxes become 6 boxes: +3 boxes = 9, so 1 box = 3. Larger = 5 × 3 = 15. Check: 9 and 15 become 18 and 24, and 18:24 = 3:4.","9/3*5"),
# Linking
("Q","Ratios: linking","If A:B = 2:3 and B:C = 3:4, what is A:C?","1:2",["2:3","3:4","3:2"],"B is 3 in both, so A:B:C = 2:3:4. A:C = 2:4 = 1:2.",None),
("Q","Ratios: linking","If A:B = 1:2 and B:C = 2:5, what is A:C?","1:5",["1:2","2:5","5:1"],"B is 2 in both, so A:B:C = 1:2:5. A:C = 1:5.",None),
("Q","Ratios: linking","If A:B = 2:3 and B:C = 5:7, what is A:C?","10:21",["2:7","6:35","3:5"],"Make B equal to 15: A:B = 10:15 and B:C = 15:21. A:C = 10:21.",None),
("Q","Ratios: linking","If A:B = 3:4 and B:C = 6:5, what is A:C?","9:10",["3:5","1:2","10:9"],"Make B equal to 12: A:B = 9:12 and B:C = 12:10. A:C = 9:10.",None),
("Q","Ratios: linking","If A:B = 4:5 and B:C = 2:3, what is A:B:C?","8:10:15",["4:5:3","8:5:6","4:10:15"],"Make B equal to 10: A:B = 8:10 and B:C = 10:15. A:B:C = 8:10:15.",None),
("Q","Ratios: linking","If A:B = 2:3 and B:C = 4:5, and A + B + C = 700, what is C?","300",["160","240","350"],"Make B equal to 12: A:B:C = 8:12:15. Total boxes = 35. 1 box = 700 ÷ 35 = 20. C = 15 × 20 = 300.","700/35*15"),
("Q","Ratios: linking","If A:B = 5:6 and B:C = 3:2, and C = 40, what is A?","50",["40","60","75"],"Make B equal to 6: B:C = 6:4, so A:B:C = 5:6:4. C is 4 boxes = 40, so 1 box = 10. A = 5 × 10 = 50.","40/4*5"),
# Ages
("Q","Ratios: ages","The ages of two brothers are in the ratio 3:4. In 5 years, the ratio will be 4:5. How old is the elder brother now?","20",["15","25","30"],"Both gaps are 1 box. The younger goes from 3 to 4 boxes: +1 box = 5 years. Elder now = 4 × 5 = 20.","4*5"),
("Q","Ratios: ages","The ages of two sisters are in the ratio 2:3. In 4 years, the ratio will be 3:4. How old is the elder sister now?","12",["8","16","20"],"Both gaps are 1 box. 2 boxes become 3 boxes: +1 box = 4 years. Elder now = 3 × 4 = 12.","3*4"),
("Q","Ratios: ages","The ages of two friends are in the ratio 5:7. In 6 years, the ratio will be 3:4. How old is the younger friend now?","30",["24","36","42"],"Gaps: 5:7 has gap 2, and 3:4 has gap 1. Change 3:4 to 6:8. Then 5 boxes become 6 boxes: +1 box = 6 years. Younger now = 5 × 6 = 30.","5*6"),
("Q","Ratios: ages","A father and son have ages in the ratio 7:2. In 10 years, the ratio will be 9:4. How old is the father now?","35",["10","40","45"],"Both gaps are 5 boxes. 7 boxes become 9 boxes: +2 boxes = 10 years, so 1 box = 5. Father now = 7 × 5 = 35.","7*5"),
("Q","Ratios: ages","The present ages of two cousins are in the ratio 3:4. Five years ago, the ratio was 2:3. How old is the younger cousin now?","15",["10","20","25"],"Both gaps are 1 box. Going back, 3 boxes become 2 boxes: −1 box = 5 years. Younger now = 3 × 5 = 15.","3*5"),
("Q","Ratios: ages","The ages of two people are in the ratio 4:5, and the sum of their ages is 54. How old will the elder be in 6 years?","36",["30","34","42"],"Total boxes = 9. 1 box = 54 ÷ 9 = 6. Elder now = 5 × 6 = 30. In 6 years = 36.","54/9*5+6"),
("Q","Ratios: ages","The ages of A and B are in the ratio 5:3, and A is 12 years older than B. How old will B be in 4 years?","22",["18","30","34"],"Extra boxes = 2. 2 boxes = 12, so 1 box = 6. B now = 3 × 6 = 18. In 4 years = 22.","12/2*3+4"),
# Other ratio
("Q","Ratios: general","What is the simplest form of 0.5 : 0.75?","2:3",["1:2","3:4","5:7"],"Multiply both by 100: 50:75. Divide both by 25: 2:3.",None),
("Q","Ratios: general","A 40-litre mixture has milk and water in the ratio 3:1. How much water must be added to make the ratio 3:2?","10 litres",["5 litres","15 litres","20 litres"],"Milk = 30 and water = 10. Milk stays 30. For 3:2, water must be 20. Add 20 − 10 = 10 litres.","20-10"),
("Q","Ratios: general","Three partners share a profit of Rs. 72,000 in the ratio 2:3:4. What is the difference between the largest and smallest shares?","Rs. 16,000",["Rs. 8,000","Rs. 24,000","Rs. 32,000"],"Total boxes = 9. 1 box = 8,000. Difference = 4 − 2 = 2 boxes = 16,000.","72000/9*2"),
("Q","Ratios: general","If 12 notebooks cost Rs. 300, what will 20 notebooks cost?","Rs. 500",["Rs. 400","Rs. 450","Rs. 600"],"1 notebook = 300 ÷ 12 = Rs. 25. 20 notebooks = 20 × 25 = 500.","300/12*20"),
("Q","Ratios: general","The angles of a triangle are in the ratio 2:3:4. What is the largest angle?","80°",["40°","60°","90°"],"Angles of a triangle add up to 180°. Total boxes = 9. 1 box = 20°. Largest = 4 × 20 = 80°.","180/9*4"),
("Q","Ratios: general","A box holds Rs. 5 and Rs. 10 coins in the ratio 3:2. The total value is Rs. 280. How many Rs. 10 coins are there?","16",["8","20","24"],"Each group of 3 Rs. 5 coins and 2 Rs. 10 coins is worth 15 + 20 = Rs. 35. Number of groups = 280 ÷ 35 = 8. Rs. 10 coins = 2 × 8 = 16.","280/35*2"),
# Analytical
("A","Conditional logic","If the report is late, the manager is angry. The manager is not angry. What can we conclude?","The report was not late.",["The report was late.","The manager will be angry later.","Nothing can be concluded."],"If P then Q. Not Q, so not P. This is the one safe backward step.",None),
("A","Conditional logic","If it is Sunday, the office is closed. The office is closed today. What can we conclude?","Nothing certain about the day.",["Today is Sunday.","Today is not Sunday.","The office will open tomorrow."],"This is the mistake you made in the diagnostic test. If P then Q does not work backward from Q to P. The office could be closed for another reason.",None),
("A","Conditional logic","Only members may vote. Sana voted. What must be true?","Sana is a member.",["All members voted.","Sana is not a member.","Nothing can be concluded."],"\"Only members may vote\" means: if you voted, you are a member.",None),
("A","Ordering","Kamran is taller than Nadir but shorter than Faisal. Imran is shorter than Nadir. Who is the second shortest?","Nadir",["Faisal","Kamran","Imran"],"Write one line, tallest first: Faisal > Kamran > Nadir > Imran. Second from the short end is Nadir.",None),
("A","Ordering","Ali finished before Babar but after Danish. Chand finished after Babar but before Ejaz. Who finished third?","Babar",["Ali","Chand","Danish"],"The order is Danish, Ali, Babar, Chand, Ejaz. Third is Babar.",None),
("A","Series","What comes next? 2, 6, 12, 20, 30, ?","42",["36","40","44"],"The gaps are 4, 6, 8, 10, then 12. 30 + 12 = 42.","30+12"),
("A","Coding","If TABLE is coded as UBCMF, how is CHAIR coded?","DIBJS",["DHBJS","BGZHQ","DIBJR"],"Each letter moves one forward: C→D, H→I, A→B, I→J, R→S.",None),
# Verbal
("V","Synonyms","Choose the closest meaning of UBIQUITOUS.","Found everywhere",["Very rare","Unclear","Hostile"],"Ubiquitous = found everywhere (ہر جگہ موجود). Root: Latin ubique, \"everywhere\".",None),
("V","Antonyms","Choose the opposite of ACRIMONIOUS.","Friendly",["Bitter","Harsh","Lengthy"],"Acrimonious = bitter and angry (تلخ). Root: acer, \"sharp\". The opposite is friendly.",None),
("V","Analogies","TACITURN : TALK. Choose the pair with the same relationship.","Stingy : Spend",["Generous : Give","Fragile : Break","Brave : Fight"],"A taciturn person is unwilling to talk. A stingy person (کنجوس) is unwilling to spend.",None),
("V","Sentence completion","Far from being ______, the ambassador's remarks were carefully chosen to ______ both sides.","impulsive; reassure",["deliberate; alarm","measured; reassure","cautious; calm"],"\"Far from\" needs the opposite of \"carefully chosen\", which is impulsive (بغیر سوچے). The remarks were chosen to reassure.",None),
("V","Grammar","Each of the delegates ______ submitted a report.","has",["have","are","were"],"\"Each\" is singular, so it takes \"has\". The word \"delegates\" does not change this.",None),
("V","Error spotting","Which part contains an error? \"The committee has agreed on the proposal, and its decision are final.\"","its decision are",["has agreed","on the proposal","final"],"\"Decision\" is singular, so it should be \"its decision is final\".",None),
]
