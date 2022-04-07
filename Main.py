#IMPORTS
import pygame # Used for game window
import sys # Used to end program
import numpy as np # Used for arrays
from Pages import settingsPage as settings
from Pages import questionPage as question
from Pages import questionsDictionary as qs # A dictionary with all the questions in it

#INITIALIZATION
pygame.init() 

#CLASSES
class Colours: # Colours to be used within the project
    BACKGROUND_C = (1, 117, 15)
    TEXT_C = (0, 0, 0)
    QUESTION_C = (1, 51, 117)
    INCORRECT_C = (255, 0, 0)
    CORRECT_C = (0, 255, 0)

class Fonts: # Fonts to be used within the project
    TITLE_F = pygame.font.SysFont('Comic Sans MS', 50)
    QUESTION_F = pygame.font.SysFont('Comic Sans MS', 30)

#VARIABLES
monitorInfo = pygame.display.Info()
clock = pygame.time.Clock() # A clock that keeps track of game time
fps = 30 # The number of frames a second the game is running at
screen = pygame.display.set_mode((monitorInfo.current_w, monitorInfo.current_h - 20)) # The screen the game is drawn on to

page = "Settings" # The page displayed to the user

ansState = "No Click"
questionAnswered = False

questionType = ""
answerType = ""

settings.initButtons(Fonts.QUESTION_F, Colours.QUESTION_C, Colours.TEXT_C, screen)
#FUNCTIONS

#MAIN
while True:
    screen.fill(Colours.BACKGROUND_C) # Initialises the screen as the background colour

    if page == "Settings":
        settings.showTitle(screen, Fonts.TITLE_F, Colours.TEXT_C, Colours.QUESTION_C) # Shows the title for the settings page

        settings.printButtons() # Shows all the buttons for the settings screen

    if page == "Questions":
        question.showQuestion(Colours.QUESTION_C, Fonts.TITLE_F, Colours.TEXT_C, screen)
        question.showAnswers(ansState, Colours.QUESTION_C, Colours.CORRECT_C, Colours.INCORRECT_C, Fonts.QUESTION_F, Colours.TEXT_C, screen)

    for event in pygame.event.get(): # Runs for each possible event in pygame
        if event.type == pygame.QUIT:
            pygame.quit() # Closes the window
            sys.exit() # Ends the program
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos() # Gets the coordinates of the mouse pointer
            
            if page == "Questions":
                if questionAnswered:
                    question.newQuestion(questionType, answerType, qs.questionsDict)
                    ansState = "No Click"
                    questionAnswered = False
                else:
                    ansState = question.detectClick(mousePos, screen)
                    questionAnswered = True
            
            if page == "Settings":
                detection = settings.detectClick(mousePos)
                if detection != "NONE":
                    questionType = detection[0]
                    answerType = detection[1]
                    question.newQuestion(questionType, answerType, qs.questionsDict)
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