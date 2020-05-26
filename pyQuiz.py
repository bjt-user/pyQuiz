import random

#the following method searches for all question positions until the randomly selected question is reached
def questionFinder():
    pos1 = 0

    for i in range(0, selectedQuestionID):
        try:
            pos1 = text.index("<question>", pos1)
            print(pos1)
            pos1 += 1
        except:
            print("index out of range")
            break
    #lastly remove the leading question tag
    pos1 += 9
    return pos1

a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)

userInputList = []

print(a)
print(b)
print(c)

#path for the open-function is entered in unix style even on windows systems

try:
    daten = open("C:/Users/whateverwhatever/Documents/unimportant_documents/quiz_questions.txt", "r")
    text = daten.read()
    daten.close()
    print(text)
except:
    print("cannot open file")


print(text.find("question"))

#prints the number of times the string "question" comes up in the file
print(text.count("question"))

numberOfQuestions = text.count("<question>")
print(numberOfQuestions)
selectedQuestionID = random.randint(1, numberOfQuestions)
print("the randomly selected question is question number " + str(selectedQuestionID))


sqid = questionFinder()
print(sqid)

endOfQuestion = text.find("</question>", sqid)
startOfAnswer = text.find("<answer>", sqid)
endOfAnswer = text.find("</quizblock>", sqid)

questionString = text[sqid:endOfQuestion]
answerString = text[(startOfAnswer+8):endOfAnswer]
answerStringList = answerString.split("<answer>")

for i in range(0, len(answerStringList)):
    answerStringList[i] = answerStringList[i].replace("\n","")
    answerStringList[i] = answerStringList[i].replace("</answer>", "")
    answerStringList[i] = answerStringList[i].replace("\"","")

print("selected question: " + questionString)
#user input
for i in range(0, len(answerStringList)):
    userInputList.append(input())


for i in range(0, len(answerStringList)):
    if userInputList[i] == answerStringList[i]:
        print("you were correct in line " + str(i))
    else:
        print("the answer in line " + str(i) + " was: " + answerStringList[i])

print(str(userInputList))
print(str(answerStringList))


#the program works so far