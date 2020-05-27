import random

def questionFinder():
    pos1 = 0

    for z in range(0, selectedQuestionID):
        try:
            pos1 = text.index("<question>", pos1)
            pos1 += 1
        except:
            print("index out of range")
            break
    #lastly remove the leading question tag
    pos1 += 9
    return pos1

userInputList = []

answeredQuestions = []

#path for the open-function is entered in unix style even on windows systems
try:
    daten = open("C:/Users/whateverwhatever/Documents/unimportant_documents/quiz_questions.txt", "r")
    text = daten.read()
    daten.close()
except:
    print("cannot open file")


numberOfQuestions = text.count("<question>")

alreadyAnswered = "firstLoop"

#Python has no static typing but you have to define variables
#and to define a variable you have to initialize it for some reason
i = 0

while True:
    # had problems with using True, False, None, so I went with Strings
    # one of Pythons weaknesses is that they change a lot of the syntax of existing languages
    # like writing True and False with startin capital letters

    selectedQuestionID = random.randint(1, numberOfQuestions)    

    if alreadyAnswered != "firstLoop":
        for j in range(0, len(answeredQuestions)):
            if selectedQuestionID == answeredQuestions[j]:
                alreadyAnswered = "yes"

    if alreadyAnswered != "yes":
        answeredQuestions.append(selectedQuestionID)
    else:
        alreadyAnswered = "blank"
        continue

    print(str(answeredQuestions))

    print("the randomly selected question is question number " + str(selectedQuestionID))
    sqid = questionFinder()

    endOfQuestion = text.find("</question>", sqid)
    startOfAnswer = text.find("<answer>", sqid)
    endOfAnswer = text.find("</quizblock>", sqid)

    questionString = text[sqid:endOfQuestion]
    answerString = text[(startOfAnswer+8):endOfAnswer]
    answerStringList = answerString.split("<answer>")

    for k in range(0, len(answerStringList)):
        answerStringList[k] = answerStringList[k].replace("\n","")
        answerStringList[k] = answerStringList[k].replace("</answer>", "")

    print("selected question: " + questionString)
    #user input
    for l in range(0, len(answerStringList)):
        userInputList.append(input())

    for n in range(0, len(answerStringList)):
        if userInputList[n] == answerStringList[n]:
            print("you were correct in line " + str(n))
        else:
            print("the answer in line " + str(n) + " was: " + answerStringList[n])

    userInputList.clear()
    i +=1
    if i == numberOfQuestions:
        break

    alreadyAnswered = "blank"


#i have to use the random.shuffle method next time to shuffle lists randomly