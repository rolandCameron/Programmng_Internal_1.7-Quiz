# This file contains the code for the questions
# Code in here will be called in "Internal_1.7_Main.py"

# IMPORTS
import pygame
import random
from Pages import questionsDictionary as qs # A dictionary with all the questions in it

global questionText
global corAnswer
global answers

xSize = 200
ySize = 50

def newQuestion(questionType, answerType):
    global answers
    global questionText
    global corAnswer

    #QUESTION
    qNum = random.randint(1, len(qs.questionsDict)) # Picks a random number for a question
    question = qs.questionsDict[qNum] # Gets the list of information for the given question

    if answerType == "Population": #Gets the correct answer to the question
        corAnswer = question[1]
    elif answerType == "Country":
        corAnswer = question[0]
    elif answerType == "Capital":
        corAnswer = question[2]

    answers = [corAnswer]

    # Code below inputs the random question into the question presets
    if questionType == "Capital":
        if answerType == "Population":
            questionText = f"Which {answerType} belongs to the same country as {question[2]}?"
        if answerType == "Country":
            questionText = f"Which {answerType} is {question[2]} in?"
    
    elif questionType == "Population":
        if answerType == "Capital":
            questionText = f"Which {answerType} belongs to a country with a population of {question[1]}?"
        if answerType == "Country":
            questionText = f"Which {answerType} has a population of {question[1]}"
    
    elif questionType == "Country":
        if answerType == "Capital":
            questionText = f"Which {answerType} belongs to {question[0]}"
        if answerType == "Population":
            questionText = f"What is the {answerType} of {question[0]}?"
    
    #ANSWERS
    if answerType == "Population": #Works out what the answers should be
        a = 1
    elif answerType == "Country":
        a = 0
    elif answerType == "Capital":
        a = 2
    
    for i in range(3):
        aNum = random.randint(1, len(qs.questionsDict)) # Picks a random number for an answer
        posAns = qs.questionsDict[aNum][a] # Gets a possible answer
        if not posAns in answers: # If the answer is not already included in the answers, this code adds it
            answers.append(posAns)

def showQuestion(bColour, font, tColour, screen): # Prints out the question
    questionPrint = font.render(questionText, False, tColour) # Defines the text object that the question will use
    pygame.draw.rect(screen, bColour, (screen.get_width()/2 - questionPrint.get_width()/2 - 25, 25, screen.get_width()/4 + questionPrint.get_width()/2, 25 + questionPrint.get_height()), 0, -1, 100, 100, 100, 100) # Draws a rect for the question to go onto
    screen.blit(questionPrint, ((screen.get_width()/2 - questionPrint.get_width()/2) + 2, 26)) # Writes the question on top of the rectangle

def showAnswers(bColour, font, tColour, screen):
    localAns = answers
    for x in range(2):
        for y in range(2):
            if len(localAns) > 1:
                randAnswer = random.randint(0, (len(localAns)-1))
                answer = localAns[randAnswer]
                localAns.remove(answer)
            else:
                answer = localAns[0]
            label = font.render(answer, False, tColour)

            topLeftX = (screen.get_width()/3)*(x + 1) # Finds the top left x of the given button
            topLeftY = screen.get_height() - (screen.get_height()/3)*(y+1) # Finds the top left y of the given button

            pygame.draw.rect(screen, bColour, (topLeftX - (xSize/2), topLeftY - (ySize/2), xSize*1.5, ySize*1.5), 0, -1, 50, 50, 50, 50)
            screen.blit(label, (topLeftX, topLeftY))