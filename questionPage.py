# This file contains the code for the questions
# Code in here will be called in "Internal_1.7_Main.py"

# IMPORTS
import pygame
import random

global questionText
global corrAnswer
global answers
global ordAns
ordAns = []

xSize = 400
ySize = 50

def newQuestion(questionType, answerType, questionsDict, qFinished):
    global answers
    global questionText
    global corrAnswer
    global ordAns

    ordAns = []

    #QUESTION
    qNum = random.randint(1, len(questionsDict)) # Picks a random number for a question
    question = questionsDict[qNum] # Gets the list of information for the given question

    if answerType == "Population": #Gets the correct answer to the question
        corrAnswer = question[1]
    elif answerType == "Country":
        corrAnswer = question[0]
    elif answerType == "Capital":
        corrAnswer = question[2]

    answers = [corrAnswer]

    # Code below inputs the random question into the question presets
    if questionType == "Capital":
        if answerType == "Population":
            questionText = f"Which {answerType} belongs to the same country as {question[2]}? [{qFinished + 1}/10] Qs Completed"
        if answerType == "Country":
            questionText = f"Which {answerType} is {question[2]} in? [{qFinished}/10] Qs Completed"
    
    elif questionType == "Population":
        if answerType == "Capital":
            questionText = f"Which {answerType} belongs to a country with a population of {question[1]}? [{qFinished + 1}/10] Qs Completed"
        if answerType == "Country":
            questionText = f"Which {answerType} has a population of {question[1]}? [{qFinished + 1}/10] Qs Completed"
    
    elif questionType == "Country":
        questionText = f"What is the {answerType} of {question[0]}? [{qFinished + 1}/10] Qs Completed"
    
    #ANSWERS
    if answerType == "Country": #Works out what type answers should be
        a = 0
    elif answerType == "Population":
        a = 1
    elif answerType == "Capital":
        a = 2
    
    for i in range(3):
        gettingAns = True
        while gettingAns:
            aNum = random.randint(1, len(questionsDict)) # Picks a random number for an answer
            possAns = questionsDict[aNum][a] # Gets a possible answer
            if not possAns in answers: # If the answer is not already included in the answers, this code adds it
                answers.append(possAns)
                gettingAns = False
    
    localAns = answers
    for i in range(4):
        if len(localAns) > 1:
            randAnswer = random.randint(0, (len(localAns)-1))
            answer = localAns[randAnswer]
            localAns.remove(answer)
        else:
            answer = localAns[0]
        ordAns.append(answer)
            

def showQuestion(bColour, font, tColour, screen): # Prints out the question
    questionPrint = font.render(questionText, False, tColour) # Defines the text object that the question will use
    pygame.draw.rect(screen, bColour, (screen.get_width()/2 - questionPrint.get_width()/2 - 25, 25, screen.get_width()/4 + questionPrint.get_width()/2, 25 + questionPrint.get_height()), 0, -1, 100, 100, 100, 100) # Draws a rect for the question to go onto
    screen.blit(questionPrint, ((screen.get_width()/2 - questionPrint.get_width()/2) + 2, 26)) # Writes the question on top of the rectangle

def unevaledAnswers(bColour, font, tColour, screen):
    ansNumber = 0
    for x in range(2):
        for y in range(2):
            answer = ordAns[ansNumber]
            label = font.render(answer, False, tColour)

            topLeftX = (screen.get_width()/3)*(x + 1) # Finds the top left x of the given button
            topLeftY = screen.get_height() - (screen.get_height()/3)*(y+1) # Finds the top left y of the given button

            pygame.draw.rect(screen, bColour, (topLeftX - (xSize/2), topLeftY - (ySize/2), xSize*1.5, ySize*1.5), 0, -1, 50, 50, 50, 50)
            screen.blit(label, (topLeftX, topLeftY))
            ansNumber += 1

def evaledAnswers(corrColour, incorrColour, font, tColour, screen):
    ansNumber = 0
    for x in range(2):
        for y in range(2):
            answer = ordAns[ansNumber]
            label = font.render(answer, False, tColour)

            topLeftX = (screen.get_width()/3)*(x + 1) # Finds the top left x of the given button
            topLeftY = screen.get_height() - (screen.get_height()/3)*(y+1) # Finds the top left y of the given button

            if answer == corrAnswer:
                pygame.draw.rect(screen, corrColour, (topLeftX - (xSize/2), topLeftY - (ySize/2), xSize*1.5, ySize*1.5), 0, -1, 50, 50, 50, 50)
            else:
                pygame.draw.rect(screen, incorrColour, (topLeftX - (xSize/2), topLeftY - (ySize/2), xSize*1.5, ySize*1.5), 0, -1, 50, 50, 50, 50)
            screen.blit(label, (topLeftX, topLeftY))
            ansNumber += 1

def showAnswers(ansEval, bColour, corrColour, incorrColour, font, tColour, screen):
    if ansEval == "No Click":
        unevaledAnswers(bColour, font, tColour, screen)
    else:
        evaledAnswers(corrColour, incorrColour, font, tColour, screen)

def detectClick(mousePos, screen):
    print(corrAnswer)
    print(mousePos)
    ansNumber = 0
    for x in range(2):
        for y in range(2):
            print(ordAns)
            print(ansNumber)
            answer = ordAns[ansNumber]

            topLeftX = (screen.get_width()/3)*(x + 1) # Finds the top left x of the given button
            topLeftY = screen.get_height() - (screen.get_height()/3)*(y+1) # Finds the top left y of the given button

            print(topLeftX, " X")
            print(topLeftY, " Y")
            if mousePos[0] > (topLeftX - (xSize/2)) and mousePos[0] < (topLeftX + xSize*1.5):
                if mousePos[1] > (topLeftY - (ySize/2)) and mousePos[1] < (topLeftY + ySize*1.5):
                    print(answer)
                    if answer == corrAnswer:
                        return "Correct"
                    else:
                        return "Incorrect"
            ansNumber += 1
    
    return "No Click"