# using 0 at the end of money array is the best idea in this entire code do check it out
# the main logic of this code lies inside the while loop.
ques = ["Which is the Lightest Noble gas out of the following?\nA. Argon\nB. Xenon\nC. Neon\nD. Krypton", "Who gave the three laws of motion?\nA. Gallelio\nB. Plankc\nC. Bohr\nD. Newton", "Which continent is Egypt located in?\nA. Africa\nB. North America\nC. Europe\nD. South America", "Which p block element is liquid at room temperature 298K\nA. Bromine\nB. Gallium\nC. Mercury\nD. Iodine", "Which of the following quantities is an intensive quantity?\nA. Resistance\nB. Emmisivity\nC. Number of Moles\nD. Mass", "Which of the following combinations do NOT show countries which ONLY come in ASIA\nA. Afganistan, Myanmar, Uzbekistan\nB. Pakistan, Japan, Yemen\nC. China, Maldives, Syria\nD. Poland, India, Indonesia", "Who sang the song 'Koi kahe kehta rahe' from 'Dil Chahta Hai'?\nA. Shankar Mahadevan, Sonu Nigham, Shaan\nB. Sonu Nigham, KK, Udit Narayan\nC. KK, Shaan, Shankar Mahadevan\nD. Udit Narayan, Shankar Mahadevan, KK", "Visual Studio is made by?\nA. Google\nB. Microsoft\nC. OpenAI\nD. Adobe", "Which of the following is NOT made by or RELATED to a FAANG company?\nA. Andriod\nB. Prime Video\nC. Photoshop\nD. Instagram","Which of the following National Institutes of Technology (NIT) does NOT belong to TIER 1\nA. Jalandar\nB. Rourkela\nC. Kurukshetra\nD. Warangal"]
ans = ["C", "D", "A", "A", "B", "D", "C", "B", "C", "A"]
money = ["10,000", "25,000", "50,000", "1,00,000", "2,50,000", "5,00,000", "10,00,000", "25,00,000", "50,00,000", "1,00,00,000", "0"] # try and find out why 0 is added at the end
checkpointQuestions = [5, None]
prizeTable = "\nFormat: QUESTION : PRIZE\n1 : 10,000\n2 : 25,000\n3 : 50,000\n4 : 1,00,000\n5 : 2,50,000 - CHECKPOINT\n6 : 5,00,000\n7 : 10,00,000\n8 : 25,00,000\n9 : 50,00,000\n10 : 1,00,00,000"
numberOfQuestions = len(ques)

"""
Format: QUESTION : PRIZE
1 : 10,000
2 : 25,000
3 : 50,000
4 : 1,00,000
5 : 2,50,000 - CHECKPOINT
6 : 5,00,000
7 : 10,00,000
8 : 25,00,000
9 : 50,00,000
10 : 1,00,00,000
"""
wonMoneyCheck = "0"
checkpointCount = 0

def askQues(qNo):
    print("Question: ",qNo,"\nPrize: ", money[qNo-1])
    print(ques[qNo-1])
    print("Please type your valid answer: A, B, C, D or QUIT")
def newline():
    print("....................................................................................................")

print("Welcome to KBC: Kaun Banega Crorepati!\nThe rules of this game are simple:\n    1. You will be asked questions and each question rewards you with certain money.\n    2. Answer the questions CAREFULLY otherwise you might lose your money.\n    3. Three Checkpoints have been kept for you. If you answer a question wrong, you will recieve the money corresponding to your latest checkpoint.\n    4. You can quit anytime and walk away with the amount of money corresponding to the latest question that you answered correctly.\n    5. To lock in correct answer, type the option letter (A, B, C, D) in CAPITAL letters.\n    6. If you want to quit, type 'QUIT' in all capital letters.\nAre you ready to play KBC? type 'yes' if you are ready or type 'prize' if you want to look at the prize matrix\n")
ready = False
while ready==False:
    start = input()
    if start=="yes":
        ready = True
    elif start=="prize":
        print(prizeTable)
        # ready = False
    if ready==False:
        print("Type 'yes' when you are ready")
newline()
print("Looks like you are ready! Best of luck and let us begin!\n")


for ongoingQues in range(1, len(ques)+1):
    print(str("Question: "+str(ongoingQues)).center(100, "."))
    print(str("Prize: "+str(money[ongoingQues-1])).center(100, "."))
    if ongoingQues == checkpointQuestions[checkpointCount]:
        print(str("CHECKPOINT QUESTION").center(100, "."))
    print(ques[ongoingQues-1])
    print("Please type your valid answer: A, B, C, D or QUIT")
    userAnswerValid = False
    while userAnswerValid == False:
        userAnswer = input()
        if userAnswer != "A" and userAnswer != "B" and userAnswer != "C" and userAnswer != "D" and userAnswer != "QUIT":
            print("Invalid Answer! Please type a valid answer: A, B, C, D or QUIT\n")
        else:
            userAnswerValid = True
        if userAnswer == "QUIT":
            print("Are you sure you want to quit? If you proceed, you will walk away with", money[ongoingQues-2])
            print("Type 'YES' if you want to quit, or anything else if you do not want to quit")
            if input()=="YES":
                print("Thank you for playing KBC! You have recieved", money[ongoingQues-2], "!! We hope to see you again!")
                exit()
            userAnswerValid = False
            print("Please type your valid answer: A, B, C, D or QUIT")
        elif userAnswer == ans[ongoingQues-1]:
            print("Congratulations! The given answer is CORRECT! You now have won a total amount of", money[ongoingQues-1])
            ongoingQues = ongoingQues + 1
        else:
            print("Oops! Looks like you answered this question WRONG! Unfortunately you are now out of this game.\nYou recieved", wonMoneyCheck, "We Hope to see you again on KBC!")
            exit()
    if ongoingQues-1 == checkpointQuestions[checkpointCount]:
        newline()
        wonMoneyCheck = money[ongoingQues-2]
        print("You have reached a CHECKPOINT! This means that even if you lost after this before reaching the next checkpoint, you will still get:", wonMoneyCheck)
        checkpointCount = checkpointCount + 1
    newline()
    print("Very well, we now will be moving on to question!")
newline()
print("CONGRATULATIONS! YOU HAVE WON KBC! THANK YOU FOR PLAYING KBC WE HOPE TO SEE YOU AGAIN!!!\nYou Recieved: 1,00,00,000")
newline()
