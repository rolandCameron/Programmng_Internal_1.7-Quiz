# This file contains the code for the questions
# Code in here will be called in "Internal_1.7_Main.py"

# IMPORTS
import pygame
import random

# VARIABLES
global questionText # The text on the current question
global corrAnswer # The correct answer to the current question
global answers # A list of all the answers on screen
global ordAns # The answers to be shown on screen in a random order

xSize = 400 # x-size of buttons and text boxes
ySize = 50 # y-size of buttons and text boxes

def newQuestion(questionType, answerType, questionsDict, qFinished): # Generates a new question
    global answers
    global questionText
    global corrAnswer
    global ordAns

    ordAns = [] # Removes the old answers from the ordAns list

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
    
    for i in range(3): # Runs for each incorecct answer needed
        gettingAns = True
        while gettingAns: 
            aNum = random.randint(1, len(questionsDict)) # Picks a random number for an answer
            possAns = questionsDict[aNum][a] # Gets a possible answer
            if not possAns in answers: # If the answer is not already included in the answers, this code adds it
                answers.append(possAns)
                gettingAns = False
    
    for i in range(4): # Runs for the 4 total answers
        if len(answers) > 1: # This is to ensure the randint function has an acceptable range (0 - 0 is not acceptable)
            answer = answers[random.randint(0, (len(answers)-1))] # Picks a random answer from the list of answers
            answers.remove(answer) # Removes the picked answer form the list so it doesn't get picked multiple times
        else: 
            answer = answers[0] # Sets the answer to the final answer remaining
        ordAns.append(answer) # Appends the random answer to the list of answers to be printed       

def showQuestion(bColour, font, tColour, screen): # Prints out the question
    questionPrint = font.render(questionText, False, tColour) # Defines the text object that the question will use
    pygame.draw.rect(screen, bColour, (screen.get_width()/2 - questionPrint.get_width()/2 - 25, 25, screen.get_width()/2 + questionPrint.get_width()/2 - 25, 25 + questionPrint.get_height()), 0, -1, 100, 100, 100, 100) # Draws a rect for the question to go onto
    screen.blit(questionPrint, ((screen.get_width()/2 - questionPrint.get_width()/2) + 2, 26)) # Writes the question on top of the rectangle

def unevaledAnswers(bColour, font, tColour, screen): # Prints the answers without their evaluation shown
    ansNumber = 0 # ansNumber is used to know what label the printed number hsould have
    for x in range(2): 
        for y in range(2):
            answer = ordAns[ansNumber] # Gets the label to be printed on the button
            label = font.render(answer, False, tColour) # Turns this label into a text object

            topLeftX = (screen.get_width()/3)*(x + 1) # Finds the top left x of the given button
            topLeftY = screen.get_height() - (screen.get_height()/3)*(y+1) # Finds the top left y of the given button

            pygame.draw.rect(screen, bColour, (topLeftX - (xSize/2), topLeftY - (ySize/2), xSize*1.5, ySize*1.5), 0, -1, 50, 50, 50, 50) # Draws the rectangle behind the button text
            screen.blit(label, (topLeftX, topLeftY)) # Writes the button text
            ansNumber += 1

def evaledAnswers(corrColour, incorrColour, font, tColour, screen): # Prints out the answers wuth their evaluation shown
    # Much of this code is duplicated from the unevaledAnswers function. This code will not be commented here
    ansNumber = 0
    for x in range(2):
        for y in range(2):
            answer = ordAns[ansNumber]
            label = font.render(answer, False, tColour)

            topLeftX = (screen.get_width()/3)*(x + 1)
            topLeftY = screen.get_height() - (screen.get_height()/3)*(y+1)

            # Draws the correct answer a different colour to the rest of the answers
            if answer == corrAnswer:
                pygame.draw.rect(screen, corrColour, (topLeftX - (xSize/2), topLeftY - (ySize/2), xSize*1.5, ySize*1.5), 0, -1, 50, 50, 50, 50)
            else:
                pygame.draw.rect(screen, incorrColour, (topLeftX - (xSize/2), topLeftY - (ySize/2), xSize*1.5, ySize*1.5), 0, -1, 50, 50, 50, 50)
            
            screen.blit(label, (topLeftX, topLeftY))
            ansNumber += 1

def showAnswers(ansEval, bColour, corrColour, incorrColour, font, tColour, screen): # Shows the answers to the question
    if ansEval == "No Click": # Runs if no answer has been clicked yet
        unevaledAnswers(bColour, font, tColour, screen)
    else: # Runs if an answer has been clicked already
        evaledAnswers(corrColour, incorrColour, font, tColour, screen)

def detectClick(mousePos, screen): # Detects what has been clicked
    # Much of this code is duplicated from unevaledAnswers function. See there for more thorough commenting
    ansNumber = 0
    for x in range(2):
        for y in range(2):
            answer = ordAns[ansNumber]

            topLeftX = (screen.get_width()/3)*(x + 1)
            topLeftY = screen.get_height() - (screen.get_height()/3)*(y+1)

            # Checks the click is within the bounds of the given button
            if mousePos[0] > (topLeftX - (xSize/2)) and mousePos[0] < (topLeftX + xSize*1.5):
                if mousePos[1] > (topLeftY - (ySize/2)) and mousePos[1] < (topLeftY + ySize*1.5):
                    if answer == corrAnswer: # Checks if the button's label is the correct answer
                        return "Correct"
                    else:
                        return "Incorrect"
            ansNumber += 1
    
    return "No Click" # Returns if no buttons were clicked