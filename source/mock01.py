ID = "mock-01"
TITLE = "Full Paper 1"
KIND = "mock"
DATE = "Weekend 7-8 Nov"
MINUTES = 120
LESSON = ""

P1 = "Foreign aid is often judged by how much money is spent rather than by what it achieves. A donor may proudly report that it built two hundred schools, yet say little about whether teachers arrived or whether children learned to read. Critics argue that this habit rewards visible projects over slower, less photogenic reforms such as training civil servants or improving tax collection. Supporters of aid reply that results are hard to measure in fragile states and that some progress is better than none. Both sides, however, increasingly agree on one point: aid works best when the receiving government helps set priorities, because projects imposed from outside rarely survive once the funding ends."

P2 = "In many dry regions, farmers have turned to groundwater because it is available whenever they need it. Cheap electricity has encouraged heavy pumping, and water tables have fallen year after year. Because this loss happens out of sight, it receives less attention than a dried-up river. Some governments have tried to meter wells, but metering often faces strong political resistance from farmers. Others have paid for efficient drip irrigation. Studies warn, however, that farmers may use the saved water to irrigate more land, leaving total water use unchanged."

SEAT = "J, K, L, M and N sit in a row in seats 1 to 5, numbered from left to right. K sits in seat 2. L sits immediately to the right of M. J sits at one end. N does not sit next to K."

WEEK = "Five meetings (Audit, Finance, HR, Legal and Sales) are held on Monday to Friday, one each day. Finance is on Wednesday. HR is on the day immediately before Legal. Audit is on a later day than Legal."

TEAM = "A team of 3 is chosen from T, U, V, W, X and Y. X must be chosen. T and U cannot both be chosen. If V is chosen, W must also be chosen."

TABLE = "Students enrolled at a college: 2021: 400; 2022: 500; 2023: 450; 2024: 600."

def p(text, q):
    return {"p": text, "q": q}

Q = [
# VERBAL 40
("V","Synonyms","Choose the closest meaning of ALACRITY.","Eagerness",["Reluctance","Sadness","Slowness"],"Alacrity = cheerful eagerness (جوش و خروش).",None),
("V","Synonyms","Choose the closest meaning of BENEVOLENT.","Kind",["Cruel","Clever","Ancient"],"Benevolent = kind (مہربان). Root: bene, \"good\", as in benefit.",None),
("V","Synonyms","Choose the closest meaning of EPHEMERAL.","Short-lived",["Everlasting","Heavenly","Secretive"],"Ephemeral = lasting a very short time (عارضی).",None),
("V","Synonyms","Choose the closest meaning of PRAGMATIC.","Practical",["Idealistic","Stubborn","Talkative"],"Pragmatic = practical (عملی).",None),
("V","Synonyms","Choose the closest meaning of SPURIOUS.","False",["Genuine","Angry","Rapid"],"Spurious = false, not genuine (جعلی).",None),
("V","Synonyms","Choose the closest meaning of ERUDITE.","Learned",["Rude","Ignorant","Careless"],"Erudite = having great knowledge (عالم). Do not confuse it with \"rude\".",None),
("V","Antonyms","Choose the opposite of ABUNDANT.","Scarce",["Plentiful","Ample","Heavy"],"Abundant = plentiful (وافر). The opposite is scarce (نایاب).",None),
("V","Antonyms","Choose the opposite of CONCILIATORY.","Hostile",["Friendly","Peaceful","Brief"],"Conciliatory = trying to make peace (مصالحانہ). The opposite is hostile.",None),
("V","Antonyms","Choose the opposite of LUCID.","Confusing",["Clear","Bright","Lazy"],"Lucid = clear and easy to understand (واضح). Root: lux, \"light\".",None),
("V","Antonyms","Choose the opposite of VERBOSE.","Concise",["Wordy","Noisy","Rude"],"Verbose = using too many words. Root: verbum, \"word\". The opposite is concise.",None),
("V","Antonyms","Choose the opposite of TENACIOUS.","Irresolute",["Persistent","Strong","Clever"],"Tenacious = holding on firmly (ثابت قدم). Irresolute = unable to decide or stick to a course.",None),
("V","Antonyms","Choose the opposite of AFFLUENT.","Poor",["Wealthy","Flowing","Proud"],"Affluent = wealthy (خوشحال). The opposite is poor.",None),
("V","Analogies","AUTHOR : NOVEL. Choose the pair with the same relationship.","Composer : Symphony",["Painter : Brush","Reader : Book","Singer : Stage"],"An author creates a novel. A composer creates a symphony.",None),
("V","Analogies","BIRD : AVIARY. Choose the pair with the same relationship.","Bee : Apiary",["Horse : Saddle","Fish : Water","Cow : Milk"],"An aviary is a place where birds are kept. An apiary is a place where bees are kept.",None),
("V","Analogies","THERMOMETER : TEMPERATURE. Choose the pair with the same relationship.","Barometer : Pressure",["Clock : Hands","Ruler : Straightness","Scale : Music"],"A thermometer measures temperature. A barometer measures air pressure.",None),
("V","Analogies","PREAMBLE : CONSTITUTION. Choose the pair with the same relationship.","Prologue : Play",["Verdict : Trial","Index : Book","Sequel : Film"],"A preamble is the opening part of a constitution. A prologue is the opening part of a play.",None),
("V","Analogies","COWARD : COURAGE. Choose the pair with the same relationship.","Liar : Honesty",["Judge : Law","Doctor : Medicine","Miser : Wealth"],"A coward lacks courage. A liar lacks honesty.",None),
("V","Analogies","TREE : FOREST. Choose the pair with the same relationship.","Soldier : Army",["Water : Ice","Pen : Ink","Teacher : Classroom"],"A forest is made up of trees. An army is made up of soldiers.",None),
("V","Sentence completion","The new law was intended to ______ corruption, but weak enforcement left the problem unchanged.","curb",["encourage","celebrate","ignore"],"\"But... unchanged\" shows the law aimed to reduce corruption. Curb = control or limit.",None),
("V","Sentence completion","Despite the evidence, the minister remained ______, refusing to change his position.","adamant",["flexible","doubtful","persuaded"],"\"Refusing to change\" tells you the answer. Adamant = refusing to change one's mind (اٹل).",None),
("V","Sentence completion","Her argument was so ______ that even her opponents accepted it.","cogent",["feeble","irrelevant","obscure"],"Cogent = clear and convincing (مدلل).",None),
("V","Sentence completion","Because the data were ______, the researchers could not reach a firm conclusion.","inconclusive",["definitive","reliable","complete"],"No firm conclusion was possible, so the data did not settle the matter.",None),
("V","Sentence completion","The treaty marked a ______ in relations between the two countries, which had been hostile for decades.","turning point",["continuation","repetition","stalemate"],"The treaty changes decades of hostility, so it is a turning point.",None),
("V","Sentence completion","The speaker's ______ remarks offended the guests, who had expected a more respectful tone.","disparaging",["courteous","flattering","modest"],"Disparaging = showing low regard for someone (تحقیر آمیز). This fits \"offended\".",None),
("V","Grammar","Hardly had we reached the station ______ the train left.","when",["than","then","while"],"The fixed pair is \"hardly... when\". \"No sooner\" is the one that takes \"than\".",None),
("V","Grammar","He is one of those officials who ______ always on time.","are",["is","was","has been"],"\"Who\" refers to \"officials\", which is plural, so it takes \"are\".",None),
("V","Grammar","The number of applicants ______ increased this year.","has",["have","are","were"],"\"The number\" is singular. \"A number of\" is the plural form.",None),
("V","Grammar","She insisted ______ paying the bill herself.","on",["at","for","to"],"The correct phrase is \"insist on\".",None),
("V","Grammar","If I ______ you, I would accept the offer.","were",["am","will be","had"],"For an imagined situation, use \"If I were you\".",None),
("V","Error spotting","Which part contains an error? \"The news were broadcast across the country on Monday evening.\"","The news were",["broadcast","across the country","on Monday evening"],"\"News\" is singular, so it should be \"The news was\".",None),
("V","Reading comprehension",p(P1,"What is the main idea of the passage?"),"Aid should be judged by results and works best with local ownership.",["Foreign aid should be stopped in fragile states.","Building schools is the best use of aid.","Results of aid are impossible to measure."],"The passage criticises judging aid by spending and ends with the shared point about the receiving government setting priorities.",None),
("V","Reading comprehension",p(P1,"Which is given as an example of a less photogenic reform?"),"Improving tax collection",["Building schools","Reporting to donors","Ending the funding"],"The passage names training civil servants and improving tax collection.",None),
("V","Reading comprehension",p(P1,"The author would most likely see \"built two hundred schools\" as:"),"an incomplete measure of success.",["proof that the aid worked.","a false claim by the donor.","the wrong type of aid in every case."],"The author points out that it says little about whether teachers arrived or children learned.",None),
("V","Reading comprehension",p(P1,"In this passage, \"photogenic\" most nearly means:"),"attractive to show in pictures",["expensive to carry out","easy to measure","popular with governments"],"Slower reforms are hard to show off, unlike a new building.",None),
("V","Reading comprehension",p(P1,"On what do critics and supporters increasingly agree?"),"The receiving government should help set priorities.",["Aid should be judged by money spent.","Progress in fragile states is easy to measure.","Aid should go only to civil servants."],"This is stated directly in the last sentence.",None),
("V","Reading comprehension",p(P2,"Why does groundwater loss receive less attention than a dried-up river?"),"It happens out of sight.",["It affects only cities.","It happens very quickly.","It is not harmful."],"This is stated directly in the third sentence.",None),
("V","Reading comprehension",p(P2,"According to the passage, what has encouraged heavy pumping?"),"Cheap electricity",["Drip irrigation","Metering of wells","Rising water tables"],"\"Cheap electricity has encouraged heavy pumping.\"",None),
("V","Reading comprehension",p(P2,"What problem with drip irrigation does the passage mention?"),"Total water use may not fall.",["It uses more electricity.","Farmers refuse to install it.","It damages the soil."],"Farmers may use the saved water on more land, leaving total use unchanged.",None),
("V","Reading comprehension",p(P2,"The author's tone is best described as:"),"concerned and cautious",["angry and accusing","cheerful and hopeful","amused and careless"],"The author reports a real problem and warns about limits of the solutions.",None),
("V","Reading comprehension",p(P2,"Which is the best title for the passage?"),"The Hidden Decline of Groundwater",["Why Rivers Dry Up","The Success of Drip Irrigation","How to Install a Water Meter"],"The whole passage is about groundwater falling out of sight and the difficulty of solving it.",None),
# ANALYTICAL 35
("A","Logical deduction","All ministers are politicians. No politician is a judge. What must be true?","No minister is a judge.",["Some ministers are judges.","All judges are politicians.","Some politicians are ministers and judges."],"Ministers sit inside politicians, and politicians share nothing with judges. So ministers share nothing with judges.",None),
("A","Logical deduction","Some teachers are writers. All writers are readers. What must be true?","Some teachers are readers.",["All teachers are readers.","All readers are writers.","No teacher is a reader."],"Those teachers who are writers must also be readers.",None),
("A","Conditional logic","If the bill passes, taxes rise. If taxes rise, exports fall. Exports did not fall. What must be true?","The bill did not pass.",["Taxes rose.","The bill passed.","Nothing can be concluded."],"Exports did not fall, so taxes did not rise, so the bill did not pass. Each step is the safe backward step.",None),
("A","Conditional logic","Either Asim or Bilal will go. Asim will not go. What must be true?","Bilal will go.",["Neither will go.","Both will go.","Nothing can be concluded."],"One of the two must go, and Asim is ruled out.",None),
("A","Conditional logic","If Omar studies, he will pass. Omar did not study. What can we conclude?","Nothing certain about whether he passed.",["He passed.","He failed.","He will study next time."],"If P then Q says nothing about what happens when P is false.",None),
("A","Conditional logic","No one without a ticket may enter. Hamid entered. Assuming the rule was followed, what must be true?","Hamid had a ticket.",["Hamid had no ticket.","Everyone with a ticket entered.","Nothing can be concluded."],"The rule means: if you entered, you had a ticket.",None),
("A","Logical deduction","All roses are flowers. Some flowers fade quickly. Does it follow that some roses fade quickly?","No, it does not follow.",["Yes, it must be true.","Yes, all roses fade quickly.","No, it proves no rose fades quickly."],"The flowers that fade quickly may not be roses. We simply do not know.",None),
("A","Conditional logic","Only graduates can apply. All applicants are interviewed. Rafiq applied. What must be true?","Rafiq is a graduate and was interviewed.",["Rafiq was interviewed but may not be a graduate.","Rafiq is a graduate but may not be interviewed.","Rafiq is neither a graduate nor interviewed."],"Applying shows he is a graduate, and all applicants are interviewed.",None),
("A","Critical reasoning","Umbrella sales rose after a new advertising campaign, so the campaign worked. Which fact most weakens this argument?","That season was unusually rainy.",["The advertisements were colourful.","The company has sold umbrellas for years.","The campaign ran on television."],"Rain offers another cause for the rise in sales.",None),
("A","Critical reasoning","\"Ali is a strong engineer, so he will be a good manager.\" What does this assume?","Strong engineers make good managers.",["Ali wants a higher salary.","Managers should not be engineers.","Ali has worked as a manager."],"The assumption is the missing link between the reason and the conclusion.",None),
("A","Critical reasoning","\"Afternoon naps improve memory.\" Which fact most strengthens this claim?","In a controlled trial, a nap group scored higher on memory tests than a similar no-nap group.",["Many people enjoy afternoon naps.","Some people sleep poorly at night.","Memory tests are common in schools."],"Only this fact compares similar groups and links naps with better memory.",None),
("A","Critical reasoning","\"Everyone I know likes the plan, so the whole country supports it.\" What is the flaw?","It relies on an unrepresentative sample.",["It uses too many numbers.","It attacks a person.","It says nothing about the plan."],"The speaker's friends may not represent the whole country.",None),
("A","Critical reasoning","A city wants to know if a new road will reduce commuting time. Which information is most useful?","Commuting times before and after a similar road elsewhere",["The colour of the road signs","The name of the construction company","The number of city parks"],"Only this directly measures the effect of a similar road on commuting time.",None),
("A","Critical reasoning","\"To reduce plastic waste, the city should ban plastic bags.\" What does this assume?","Plastic bags form a meaningful part of plastic waste.",["All plastic can be recycled.","Residents dislike shopping.","The city has no other waste."],"If bags were a tiny share of waste, the ban would achieve little.",None),
("A","Critical reasoning","\"School A has the highest test scores, so it has the best teachers.\" Which fact most weakens this argument?","School A admits only students who already score highly.",["School A has a large library.","School A is the oldest school.","Teachers at School A wear uniforms."],"This gives another explanation for the high scores.",None),
("A","Seating puzzle",p(SEAT,"Who sits in seat 3?"),"M",["J","L","N"],"Try M3, L4: N must not touch K, so N5 and J1. Try M4, L5: J1 and N3, but N touches K, so this fails. The order is J, K, M, L, N.",None),
("A","Seating puzzle",p(SEAT,"Who sits at the right end?"),"N",["J","K","L"],"The order is J, K, M, L, N.",None),
("A","Seating puzzle",p(SEAT,"Who sits between K and L?"),"M",["J","N","No one"],"The order is J, K, M, L, N.",None),
("A","Ordering","P is heavier than Q. R is lighter than Q. S is heavier than P. Who is the lightest?","R",["P","Q","S"],"Heaviest first: S > P > Q > R.",None),
("A","Ordering puzzle",p(WEEK,"On which day is HR?"),"Monday",["Tuesday","Thursday","Friday"],"HR and Legal need two days in a row, either Mon-Tue or Thu-Fri. If Legal is on Friday, Audit cannot be later. So HR is Monday and Legal is Tuesday.",None),
("A","Ordering puzzle",p(WEEK,"Which must be true?"),"Legal is on Tuesday.",["Audit is on Thursday.","Sales is on Friday.","Legal is on Friday."],"Audit and Sales can take Thursday and Friday in either order, so only Legal's day is fixed.",None),
("A","Grouping puzzle",p(TEAM,"Which team is valid?"),"X, V, W",["T, U, X","X, V, Y","T, V, W"],"T, U, X has T and U together. X, V, Y has V without W. T, V, W leaves out X.",None),
("A","Grouping puzzle",p(TEAM,"If V is chosen, who are the other two?"),"W and X",["T and X","X and Y","W and Y"],"X must serve, and V requires W. That fills all three places.",None),
("A","Grouping puzzle",p(TEAM,"If T is chosen, who could be the third member?"),"W",["U","V","No one else can serve"],"T and X take two places. U cannot join T. V would also need W, which makes four. W works.",None),
("A","Grouping puzzle",p(TEAM,"How many different valid teams are possible?"),"6",["4","5","7"],"X is fixed. Valid pairs: TW, TY, UW, UY, VW, WY. That makes 6.","6"),
("A","Blood relations","A man says of a boy, \"He is the son of my mother's only son.\" How is the boy related to the man?","Son",["Brother","Nephew","Cousin"],"The man's mother's only son is the man himself. So the boy is his son.",None),
("A","Blood relations","Rashid's father is Nasir's only son. How is Nasir related to Rashid?","Grandfather",["Father","Uncle","Brother"],"Nasir is the father of Rashid's father.",None),
("A","Blood relations","Zainab is the daughter of Hamza's sister. How is Hamza related to Zainab?","Maternal uncle",["Father","Paternal uncle","Brother"],"Hamza is her mother's brother, which makes him her maternal uncle (ماموں).",None),
("A","Directions","A man walks 6 km east, turns left and walks 8 km. How far is he from his starting point?","10 km",["8 km","12 km","14 km"],"Use a right-angled triangle: √(6² + 8²) = √100 = 10.","(6*6+8*8)**0.5"),
("A","Directions","A woman faces north. She turns 90° right, then 180°, then 90° left. Which way does she face now?","South",["North","East","West"],"North → east → west → south. Turning left from west gives south.",None),
("A","Directions","A man walks 4 km south, turns right and walks 3 km, then turns right and walks 4 km. Where is he now?","3 km west of the start",["3 km east of the start","4 km north of the start","7 km west of the start"],"South, then right is west, then right is north. The 4 km south and north cancel, leaving 3 km west.",None),
("A","Coding","If GOLD is coded as HPME, how is SILK coded?","TJML",["TJMK","RHKJ","TJLM"],"Each letter moves one forward: S→T, I→J, L→M, K→L.",None),
("A","Coding","If sky is called water, water is called road, and road is called tree, where do fish live?","Road",["Water","Sky","Tree"],"Fish live in water, and water is called road.",None),
("A","Series","What comes next? 7, 10, 8, 11, 9, 12, ?","10",["13","14","15"],"The pattern is +3, −2, repeated. 12 − 2 = 10.","12-2"),
("A","Series","What comes next? A, C, F, J, O, ?","U",["S","T","V"],"The gaps are +2, +3, +4, +5, then +6. O is letter 15, and 15 + 6 = 21, which is U.",None),
# QUANT 25
("Q","Percentages","An item priced at Rs. 800 goes up by 15%. What is the new price?","Rs. 920",["Rs. 815","Rs. 880","Rs. 950"],"15% of 800 = 120. 800 + 120 = 920.","800*1.15"),
("Q","Percentages","A price rises by 20% and then falls by 20%. What is the overall change?","4% decrease",["No change","4% increase","10% decrease"],"Start at 100. Up 20% gives 120. Down 20% of 120 gives 96. That is a 4% decrease.",None),
("Q","Percentages","An item bought for Rs. 400 is sold for Rs. 500. What is the profit percentage?","25%",["20%","30%","50%"],"Profit = 100. Always divide by the cost: 100 ÷ 400 = 25%.","100/400*100"),
("Q","Percentages","30 is what percentage of 120?","25%",["20%","30%","40%"],"30 ÷ 120 × 100 = 25%.","30/120*100"),
("Q","Ratios","Rs. 63,000 is divided in the ratio 4:5. What is the larger share?","Rs. 35,000",["Rs. 7,000","Rs. 28,000","Rs. 45,000"],"Total boxes = 9. 1 box = 7,000. Larger = 5 × 7,000 = 35,000.","63000/9*5"),
("Q","Ratios: linking","If A:B = 3:5 and B:C = 2:3, what is A:C?","2:5",["1:1","3:5","6:5"],"Make B equal to 10: A:B = 6:10 and B:C = 10:15. A:C = 6:15 = 2:5.",None),
("Q","Ratios: difference","Two numbers are in the ratio 5:8, and their difference is 18. What is the smaller number?","30",["18","40","48"],"Extra boxes = 3. 1 box = 6. Smaller = 5 × 6 = 30.","18/3*5"),
("Q","Averages","The average of 6 numbers is 15. If the number 20 is removed, what is the new average?","14",["13","15","16"],"Total = 90. After removing 20, the total is 70 for 5 numbers. 70 ÷ 5 = 14.","(6*15-20)/5"),
("Q","Averages","A student's average over 5 tests is 72. What must she score in the 6th test for an average of 75?","90",["75","78","85"],"Needed total = 6 × 75 = 450. Current total = 5 × 72 = 360. 450 − 360 = 90.","6*75-5*72"),
("Q","Statistics","What is the median of 3, 9, 4, 7, 12?","7",["4","6","9"],"Put them in order: 3, 4, 7, 9, 12. The middle value is 7.","7"),
("Q","Speed","A car travels at 60 km/h for 2.5 hours. How far does it go?","150 km",["120 km","140 km","160 km"],"Distance = speed × time = 60 × 2.5 = 150.","60*2.5"),
("Q","Work","12 workers finish a job in 10 days. How long would 8 workers take?","15 days",["8 days","12 days","20 days"],"Total work = 12 × 10 = 120 worker-days. 120 ÷ 8 = 15.","12*10/8"),
("Q","Work","A can finish a job in 6 days and B can finish it in 12 days. How long will they take together?","4 days",["3 days","8 days","9 days"],"Each day: 1/6 + 1/12 = 3/12 = 1/4. So 4 days.","1/(1/6+1/12)"),
("Q","Speed","A car goes to a city at 60 km/h and returns on the same road at 40 km/h. What is the average speed for the whole trip?","48 km/h",["45 km/h","50 km/h","52 km/h"],"Do not simply average them. Take a 120 km distance: 2 hours going and 3 hours back. 240 km ÷ 5 hours = 48.","240/5"),
("Q","Algebra","If 3x − 7 = 14, what is x?","7",["5","6","8"],"3x = 21, so x = 7.","21/3"),
("Q","Algebra","If x + y = 12 and x − y = 4, what is xy?","32",["16","24","48"],"Adding gives 2x = 16, so x = 8 and y = 4. xy = 32.","8*4"),
("Q","Algebra","What is the sum of the two values of x in x² − 9x + 20 = 0?","9",["−9","1","20"],"Factors: (x − 4)(x − 5) = 0. So x = 4 or 5. Sum = 9.","4+5"),
("Q","Algebra","3 pens and a notebook cost Rs. 110. 1 pen and a notebook cost Rs. 70. What is the price of one pen?","Rs. 20",["Rs. 10","Rs. 30","Rs. 40"],"The difference is 2 pens = Rs. 40. So 1 pen = Rs. 20.","(110-70)/2"),
("Q","Geometry","Two angles of a triangle are 50° and 60°. What is the third angle?","70°",["60°","80°","110°"],"Angles add up to 180°. 180 − 50 − 60 = 70.","180-50-60"),
("Q","Geometry","A rectangle has a perimeter of 36 cm and a length of 12 cm. What is its area?","72 sq cm",["36 sq cm","48 sq cm","144 sq cm"],"Length + width = 36 ÷ 2 = 18. Width = 6. Area = 12 × 6 = 72.","12*(36/2-12)"),
("Q","Geometry","A circle has a radius of 7 cm. What is its area? (Use π = 22/7.)","154 sq cm",["44 sq cm","88 sq cm","308 sq cm"],"Area = πr² = 22/7 × 49 = 154.","22/7*49"),
("Q","Data interpretation",p(TABLE,"What was the percentage increase from 2021 to 2022?"),"25%",["10%","20%","100%"],"Increase = 100. Divide by the starting value: 100 ÷ 400 = 25%.","100/400*100"),
("Q","Data interpretation",p(TABLE,"What was the average enrolment over the four years?"),"487.5",["450","475","500"],"Total = 1,950. 1,950 ÷ 4 = 487.5.","(400+500+450+600)/4"),
("Q","Probability","A bag has 4 red and 6 blue balls. One is picked at random. What is the probability that it is red?","2/5",["1/4","2/3","3/5"],"4 red out of 10 balls = 4/10 = 2/5.",None),
("Q","Probability","Two fair coins are tossed. What is the probability of two heads?","1/4",["1/8","1/3","1/2"],"The outcomes are HH, HT, TH, TT. One out of four is HH.",None),
]
