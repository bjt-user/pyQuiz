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

def userInput(answerStringList, userInputList):
    userAction = ""
    for l in range(0, len(answerStringList)):
        newInput = input()
        userInputList.append(newInput)
        if newInput == "quit":
            userAction = "quit"
            break
            
    return userAction

    

userInputList = []

answeredQuestions = []

points = 0

mistakes = 0

#booleans seem to be case sensitive and None for defining a bool with no value

#path for the open-function is entered in unix style even on windows systems

try:
    daten = open("C:/Users/whatever/Documents/unimportant_documents/m_und_a.txt", "r")
    text = daten.read()    
except:
    print("cannot open file")

daten.close()


numberOfQuestions = text.count("<question>")

alreadyAnswered = "firstLoop"

#Python has no static typing but you have to define variables (Python weirdness)
#and to define a variable you have to initialize it for some reason
#i have to try to get into a python shell again some time
i = 0

while True:
    # it seems to be impossible to only answer a question once
    # booleans may be broken in Python, so I try it with Strings
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
    userAction = userInput(answerStringList, userInputList)
    if userAction == "quit":
        print("you have quit the program")
        break

    for n in range(0, len(answerStringList)):
        if userInputList[n] == answerStringList[n]:
            print("you were correct in line " + str(n))
            points += 1
        else:
            print("the answer in line " + str(n) + " was: " + answerStringList[n])
            mistakes += 1


    print("You have " + str(points) + " points. You made " + str(mistakes) + " mistakes.")
    print()

    userInputList.clear()
    i +=1
    if i == numberOfQuestions:
        break

    alreadyAnswered = "blank"


input()


#the program works so far
#i have to use the random.shuffle method next time
#but i had to proove that i could do it this way

#issue1: Antworten, die sich über mehrere Zeilen erstrecken
#eine Lösung könnte sein, die userInputList und die answerStringList jeweils in einen String umzuwandeln und dann zu vergleichen ob sie übereinstimmen
#so wäre es dann egal wann man in einer Antwort den Zeilenumbruch macht
#wobei das wiederum bei mehrteiligen Antworten, die klar voneinander abzugrenzen sind, nicht so gut wäre

#oder ich mache einfach in der quizdatei einen Zeilenumbruch und replace einfach "\n" mit "" und schließe den answer-tag erst nach mehreren Zeilen,
#wenn die Antwort wirklich zuende ist
#nur wie mache ich das dann beim Userinput?

#TODO: print number of current question