#IMPORTS
import pygame # Used for game window
import sys # Used to end program
import numpy as np # Used for arrays
from Pages import settingsPage as settings
from Pages import questionPage as question
from Pages import questionsDictionary as qs # A dictionary with all the questions in it
from Pages import statisticsPage as stats

#INITIALIZATION
pygame.init() 

#CLASSES
class Colours: # Colours to be used within the project
    BACKGROUND_C = (70, 36, 76)
    TEXT_C = (0, 0, 0)
    QUESTION_C = (212, 155, 84)
    INCORRECT_C = (113, 43, 117)
    CORRECT_C = (199, 75, 80)

class Fonts: # Fonts to be used within the project
    TITLE_F = pygame.font.SysFont('Comic Sans MS', 50)
    QUESTION_F = pygame.font.SysFont('Comic Sans MS', 30)

#VARIABLES
monitorInfo = pygame.display.Info()
clock = pygame.time.Clock() # A clock that keeps track of game time
fps = 30 # The number of frames a second the game is running at
screen = pygame.display.set_mode((monitorInfo.current_w, monitorInfo.current_h - 20)) # The screen the game is drawn on to

global page # The page displayed to the user

global ansState
global questionAnswered
global questionsFinished
global numQCorr
global totalNumQCompleted

global questionType
global answerType

page = "Settings" 

ansState = "No Click"
questionAnswered = False
questionsFinished = 0
numQCorr = 0
totalNumQCompleted = 0

questionType = ""
answerType = ""

settings.initButtons(Fonts.QUESTION_F, Colours.QUESTION_C, Colours.TEXT_C, screen)
#FUNCTIONS
def softReset(): # To be called when a player wishes to restart the same quiz
    global questionsFinished
    global ansState
    global questionAnswered
    global page

    questionsFinished = 0
    ansState = "No Click"
    questionAnswered = False

    question.newQuestion(questionType, answerType, qs.questionsDict, questionsFinished)
    page = "Questions"

def hardReset(): # To be called when the player wishes to change settings
    global questionType
    global answerType
    global numQCorr
    global totalNumQCompleted
    global page

    softReset()
    questionType = ""
    answerType = ""

    numQCorr = 0
    totalNumQCompleted = 0

    page = "Settings"

#MAIN
while True:
    screen.fill(Colours.BACKGROUND_C) # Initialises the screen as the background colour

    if page == "Settings":
        settings.showTitle(screen, Fonts.TITLE_F, Colours.TEXT_C, Colours.QUESTION_C) # Shows the title for the settings page

        settings.printButtons() # Shows all the buttons for the settings screen

    if page == "Questions":
        question.showQuestion(Colours.QUESTION_C, Fonts.TITLE_F, Colours.TEXT_C, screen)
        question.showAnswers(ansState, Colours.QUESTION_C, Colours.CORRECT_C, Colours.INCORRECT_C, Fonts.QUESTION_F, Colours.TEXT_C, screen)

    if page == "Statistics":
        stats.showStatistics(totalNumQCompleted, numQCorr, Colours.QUESTION_C, Colours.TEXT_C, Fonts.TITLE_F, screen)
        stats.showButtons(Colours.QUESTION_C, Colours.TEXT_C, Fonts.TITLE_F, screen)

    for event in pygame.event.get(): # Runs for each possible event in pygame
        if event.type == pygame.QUIT:
            pygame.quit() # Closes the window
            sys.exit() # Ends the program
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos() # Gets the coordinates of the mouse pointer
            
            if page == "Statistics":
                click = stats.detectClick(mousePos, screen)
                if click != "No Click":
                    if click == 0:
                        softReset()
                    elif click == 1:
                        hardReset()
                    elif click == 2:
                        pygame.quit() # Closes the window
                        sys.exit() # Ends the program
                    print(click)
                    print(page)

            if page == "Questions":
                if questionAnswered:
                    question.newQuestion(questionType, answerType, qs.questionsDict, questionsFinished)
                    ansState = "No Click"
                    questionAnswered = False
                    questionsFinished += 1
                    if questionsFinished == 10:
                        page = "Statistics"
                else:
                    ansState = question.detectClick(mousePos, screen)
                    if ansState == "Correct":
                        numQCorr += 1
                    
                    if ansState != "No Click":
                        totalNumQCompleted += 1
                        questionAnswered = True
            
            if page == "Settings":
                detection = settings.detectClick(mousePos)
                if detection != "NONE":
                    questionType = detection[0]
                    answerType = detection[1]
                    questionsFinished += 1
                    question.newQuestion(questionType, answerType, qs.questionsDict, questionsFinished)
                    page = "Questions"

    pygame.display.flip() # Updates the screen
    clock.tick(fps) # Waits for "fps" milliseconds

#DECOMPOSITION
"""
1. Present options for the topic of the quiz
    a. Create a pygame screen
    b. Present buttons for each of the answers and questions available (Population - Capital, Capital - Population, Country - Population, etc...)
    c. Detect a click on these buttons
    d. Have the user confirm their selection, do not let them select the same answer and question eg. (flag - flag, capital - capital)

2. Present questions one by one, with the desired answer option
    a. Present a question, with the related images
    b. Allow the user to answer in their chosen way
    c. Once the answer has been evaluated, move onto the next question

3. Once all the questions have been answered, give the user a score
    a. Present an end screen
    b. Show the user their score and percentage they got correct
    c. Display their answers, and which ones were correct

4. Ask if the user wants to do another quiz
    a. Allow the user to decide whether or not they want to play again
    b. Let them choose either the same quiz, or to change some of the parameters
"""