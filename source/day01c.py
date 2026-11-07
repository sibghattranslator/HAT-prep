ID = "day-01c"
TITLE = "Day 1 Retest 2: Ratios"
KIND = "daily"
DATE = "Sat 7 Nov"
MINUTES = 48

LESSON = """
<h3>Before you start</h3>
<pre>1. Find one box.
2. Use the boxes the question needs.
3. Write NOW, LATER or AGO next to age questions.
4. Ask: is this number exactly what the last line asks for?</pre>
<p><b>Coins:</b> find the value of one group first. <b>Coding:</b> check the direction with the first letter. <b>Grammar:</b> find the subject next to the verb.</p>
<p>Aim for about 70 seconds a question, so you finish with time to check.</p>
"""

Q = [
# Difference
("Q","Ratios: difference","Two numbers are in the ratio 4:9, and their difference is 40. What is the larger number?","72",["32","64","80"],"Extra boxes = 5. 1 box = 8. Larger = 9 × 8 = 72.","40/5*9"),
("Q","Ratios: difference","Two numbers are in the ratio 3:10, and their difference is 49. What is the smaller number?","21",["7","49","70"],"Extra boxes = 7. 1 box = 7. Smaller = 3 × 7 = 21.","49/7*3"),
("Q","Ratios: difference","Two numbers are in the ratio 5:7, and their difference is 18. What is their sum?","108",["45","63","90"],"Extra boxes = 2. 1 box = 9. Sum = 12 boxes = 12 × 9 = 108. 63 is only the larger number.","18/2*12"),
("Q","Ratios: difference","The savings of P and Q are in the ratio 8:3. P has saved Rs. 25,000 more than Q. What is P's saving?","Rs. 40,000",["Rs. 15,000","Rs. 25,000","Rs. 55,000"],"Extra boxes = 5. 1 box = 5,000. P = 8 × 5,000 = 40,000.","25000/5*8"),
("Q","Ratios: difference","Boys and girls at a school are in the ratio 7:4. There are 45 more boys than girls. How many students are there in total?","165",["60","105","180"],"Extra boxes = 3. 1 box = 15. Total boxes = 11. Total = 11 × 15 = 165.","45/3*11"),
("Q","Ratios: difference","Two numbers are in the ratio 3:8, and their difference is 35. What is their sum?","77",["21","56","63"],"Extra boxes = 5. 1 box = 7. Sum = 11 boxes = 77. 56 is only the larger number.","35/5*11"),
("Q","Ratios: difference","Two numbers are in the ratio 2:3. When 6 is subtracted from each, the ratio becomes 1:2. What is the larger original number?","18",["6","12","24"],"Gaps: 2:3 has gap 1, and 1:2 has gap 1. The gaps match. 2 boxes become 1 box: −1 box = 6. Larger = 3 × 6 = 18. Check: 12 and 18 become 6 and 12, and 6:12 = 1:2.","3*6"),
# Linking
("Q","Ratios: linking","If A:B = 5:6 and B:C = 6:11, what is A:C?","5:11",["5:6","6:11","11:5"],"B is 6 in both, so A:B:C = 5:6:11. A:C = 5:11.",None),
("Q","Ratios: linking","If A:B = 2:5 and B:C = 3:7, what is A:C?","6:35",["2:7","10:21","3:5"],"Make B equal to 15: A:B = 6:15 and B:C = 15:35. A:C = 6:35.",None),
("Q","Ratios: linking","If P:Q = 7:4 and Q:R = 6:5, what is P:R?","21:10",["7:5","10:21","28:30"],"Make Q equal to 12: P:Q = 21:12 and Q:R = 12:10. P:R = 21:10.",None),
("Q","Ratios: linking","If A:B = 2:3 and B:C = 2:3, what is A:B:C?","4:6:9",["2:3:3","2:6:9","4:3:9"],"Make B equal to 6: A:B = 4:6 and B:C = 6:9. A:B:C = 4:6:9.",None),
("Q","Ratios: linking","If A:B = 1:3 and B:C = 2:5, and A + B + C = 230, what is B?","60",["20","90","150"],"Make B equal to 6: A:B = 2:6 and B:C = 6:15. A:B:C = 2:6:15. Total boxes = 23. 1 box = 10. B = 6 × 10 = 60.","230/23*6"),
("Q","Ratios: linking","If A:B = 3:7 and B:C = 14:5, and C = 50, what is A?","60",["30","70","140"],"Make B equal to 14: A:B = 6:14. So A:B:C = 6:14:5. C is 5 boxes = 50, so 1 box = 10. A = 6 × 10 = 60.","50/5*6"),
("Q","Ratios: linking","If A:B = 4:5 and B:C = 10:3, what is A:C?","8:3",["4:3","3:8","2:3"],"Make B equal to 10: A:B = 8:10. So A:B:C = 8:10:3. A:C = 8:3.",None),
# Ages
("Q","Ratios: ages","The ages of two friends are in the ratio 7:8. In 5 years, the ratio will be 8:9. How old is the younger friend NOW?","35",["40","45","30"],"Both gaps are 1 box. +1 box = 5 years. Younger now = 7 × 5 = 35. 40 is the younger's age later.","7*5"),
("Q","Ratios: ages","The ages of two sisters are in the ratio 2:3. In 5 years, the ratio will be 3:4. How old will the elder sister be in 5 years?","20",["10","15","25"],"Both gaps are 1 box. +1 box = 5 years. Elder now = 3 × 5 = 15. In 5 years = 20. This time the question asks about LATER.","3*5+5"),
("Q","Ratios: ages","The ages of two people are in the ratio 3:7. In 4 years, the ratio will be 1:2. How old is the younger NOW?","12",["16","28","32"],"Gaps: 3:7 has gap 4, and 1:2 has gap 1. Change 1:2 to 4:8. Then 3 boxes become 4 boxes: +1 box = 4 years. Younger now = 3 × 4 = 12. 16 is the younger's age LATER. Check: 12 and 28 become 16 and 32, and 16:32 = 1:2.","3*4"),
("Q","Ratios: ages","An uncle and nephew have ages in the ratio 5:2. In 9 years, the ratio will be 2:1. How old is the uncle NOW?","45",["18","54","63"],"Gaps: 5:2 has gap 3, and 2:1 has gap 1. Change 2:1 to 6:3. Then 5 boxes become 6 boxes: +1 box = 9 years. Uncle now = 5 × 9 = 45. Check: 45 and 18 become 54 and 27, and 54:27 = 2:1.","5*9"),
("Q","Ratios: ages","The present ages of two brothers are in the ratio 5:7. Eight years ago, the ratio was 3:5. How old is the elder brother NOW?","28",["12","20","36"],"Both gaps are 2 boxes. Going back, 5 boxes become 3 boxes: −2 boxes = 8 years, so 1 box = 4. Elder now = 7 × 4 = 28. 20 is his age 8 years AGO.","7*4"),
("Q","Ratios: ages","The ages of two people are in the ratio 3:4, and the sum of their ages is 56. How old was the younger 5 years AGO?","19",["24","29","32"],"Total boxes = 7. 1 box = 8. Younger now = 3 × 8 = 24. Five years ago = 19. 24 is the trap.","56/7*3-5"),
("Q","Ratios: ages","The ages of A and B are in the ratio 6:5, and A is 4 years older than B. How old will B be in 10 years?","30",["20","24","34"],"Extra boxes = 1. 1 box = 4. B now = 5 × 4 = 20. In 10 years = 30.","4*5+10"),
# General
("Q","Ratios: general","What is the simplest form of 0.4 : 1.2?","1:3",["1:2","2:3","4:3"],"Multiply both by 10: 4:12. Divide both by 4: 1:3.",None),
("Q","Ratios: general","A 45-litre mixture has milk and water in the ratio 4:1. How much water must be added to make the ratio 3:2?","15 litres",["9 litres","12 litres","24 litres"],"Total boxes = 5, so 1 box = 9. Milk = 36 and water = 9. Milk stays 36. For 3:2, 3 boxes = 36, so 1 box = 12 and water must be 24. Add 24 − 9 = 15 litres.","24-9"),
("Q","Ratios: general","Three brothers share Rs. 60,000 in the ratio 3:4:5. What is the smallest share?","Rs. 15,000",["Rs. 5,000","Rs. 20,000","Rs. 25,000"],"Total boxes = 12. 1 box = 5,000. Smallest = 3 × 5,000 = 15,000. 5,000 is only one box.","60000/12*3"),
("Q","Ratios: general","If 9 books cost Rs. 1,350, what will 4 books cost?","Rs. 600",["Rs. 450","Rs. 540","Rs. 900"],"1 book = 1,350 ÷ 9 = Rs. 150. 4 books = 4 × 150 = 600.","1350/9*4"),
("Q","Ratios: general","The angles of a triangle are in the ratio 1:4:7. What is the middle angle?","60°",["15°","105°","120°"],"Total boxes = 12. 1 box = 15°. Middle = 4 × 15 = 60°. 105° is the largest.","180/12*4"),
("Q","Ratios: general","A box holds Rs. 5 and Rs. 20 notes in the ratio 4:1. The total value is Rs. 400. How many Rs. 5 notes are there?","40",["10","20","80"],"One group = 4 Rs. 5 notes + 1 Rs. 20 note = 20 + 20 = Rs. 40. Groups = 400 ÷ 40 = 10. Rs. 5 notes = 4 × 10 = 40. 80 is 400 ÷ 5, which forgets the Rs. 20 notes.","400/40*4"),
# Analytical
("A","Conditional logic","If the shop is open, the lights are on. The lights are off. What can we conclude?","The shop is not open.",["The shop is open.","The lights will come on.","Nothing can be concluded."],"If P then Q. Not Q, so not P.",None),
("A","Conditional logic","If a student cheats, the student fails. Rehan failed. What can we conclude?","Nothing certain about cheating.",["Rehan cheated.","Rehan did not cheat.","Rehan will cheat again."],"You cannot go backward from Q to P. Rehan may have failed for another reason.",None),
("A","Conditional logic","Only citizens may hold the post. Kashif holds the post. What must be true?","Kashif is a citizen.",["All citizens hold posts.","Kashif is not a citizen.","Nothing can be concluded."],"\"Only citizens may hold\" means: if you hold the post, you are a citizen.",None),
("A","Ordering","Jamal is heavier than Kamal but lighter than Lal. Moin is lighter than Kamal. Who is the second heaviest?","Jamal",["Lal","Kamal","Moin"],"Heaviest first: Lal > Jamal > Kamal > Moin.",None),
("A","Ordering","Nida arrived after Omar but before Pari. Qasim arrived after Pari but before Rida. Who arrived fourth?","Qasim",["Pari","Nida","Rida"],"The order is Omar, Nida, Pari, Qasim, Rida. Fourth is Qasim.",None),
("A","Series","What comes next? 1, 4, 9, 16, 25, ?","36",["30","34","49"],"These are square numbers: 1², 2², 3², 4², 5², then 6² = 36.","6*6"),
("A","Coding","If CLOUD is coded as DMPVE, how is RIVER coded?","SJWFS",["QHUDQ","SJWFR","SIWFS"],"C→D shows each letter moves one step FORWARD. R→S, I→J, V→W, E→F, R→S. QHUDQ moves backward, which is the trap.",None),
# Verbal
("V","Synonyms","Choose the closest meaning of METICULOUS.","Very careful",["Careless","Quick","Noisy"],"Meticulous = showing great attention to detail (نہایت محتاط).",None),
("V","Antonyms","Choose the opposite of FERVENT.","Indifferent",["Passionate","Hot","Eager"],"Fervent = showing strong feeling (پرجوش). Passionate and eager are synonym traps.",None),
("V","Analogies","GENEROUS : SHARE. Choose the pair with the same relationship.","Curious : Ask",["Lazy : Work","Shy : Speak","Calm : Shout"],"A generous person tends to share. A curious person tends to ask. The others are things those people avoid.",None),
("V","Sentence completion","Far from being ______, his plan was simple enough for a child to follow.","complicated",["simple","clear","easy"],"\"Far from\" needs the opposite of \"simple enough for a child\".",None),
("V","Grammar","Either the manager or the clerks ______ responsible for the error.","are",["is","was","has"],"With either...or, the verb agrees with the nearer subject. \"Clerks\" is plural, so it takes \"are\".",None),
("V","Error spotting","Which part contains an error? \"The company has opened a new branch, and its profits has doubled.\"","its profits has",["has opened","a new branch","doubled"],"\"Profits\" is plural, so it should be \"its profits have doubled\". \"Its\" belongs to the company.",None),
]
