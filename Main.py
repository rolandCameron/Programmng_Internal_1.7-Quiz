#IMPORTS
import pygame # Used for game window
import sys # Used to end program
import numpy as np # Used for arrays
from Pages import settingsPage as settings # The settings page code
from Pages import questionPage as question # The questions page code
from Pages import questionsDictionary as qs # A dictionary with all the questions in it
from Pages import statisticsPage as stats # The statistics page code

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

global ansState # What the user has clicked on, used on the question page
global questionAnswered # Whether or not the user has answered the current question
global questionsFinished # How many questions the user has completed of this set (sets are 10 long)
global numQCorr # The total number of questions the user has gotten correct in this session
global totalNumQCompleted # The total number of questions the user has answered in this session

global questionType # What the user wants to be asked
global answerType # What the user wants to answer with

page = "Settings" # The program starts on the settings page

ansState = "No Click" # There shouldn't be anything clicked by default
questionAnswered = False # The question should be unanswered by default
questionsFinished = 0 
numQCorr = 0
totalNumQCompleted = 0

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

    # Generates a new question for the user to see
    question.newQuestion(questionType, answerType, qs.questionsDict, questionsFinished)
    page = "Questions" # Puts the user back into the quiz

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

    page = "Settings" # Puts the user back to the settings page

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
            
            if page == "Statistics": # The clicking logic if the user is on the settings page
                click = stats.detectClick(mousePos, screen) # Works out what the user has clicked
                if click != "No Click": # Runs if the user has clicked something
                    if click == 0: # Runs if the user clicked "Same Quiz?"
                        softReset() 
                    elif click == 1: # Runs if the user clicked "Settings Page"
                        hardReset()
                    elif click == 2: # Runs if the user clicked "Quit"
                        pygame.quit() # Closes the window
                        sys.exit() # Ends the program

            if page == "Questions": # The clicking logic if the user is on the questions page
                if questionAnswered: # Checks if the question on screen has been answered yet
                    question.newQuestion(questionType, answerType, qs.questionsDict, questionsFinished) # Generates a new questions
                    ansState = "No Click" # Sets the answer clicked to none
                    questionAnswered = False # Sets the new question as being unanswered
                    if questionsFinished == 10: # Stops the quiz and moves to the statistics page if the user has completed 10 questions
                        page = "Statistics"
                else:
                    ansState = question.detectClick(mousePos, screen) # Checks what the user clicked on
                    if ansState == "Correct": # Increases the number of questions answered correctly by one
                        numQCorr += 1
                    
                    if ansState != "No Click": # Runs if the user clicked on a button
                        totalNumQCompleted += 1 # Increases the total number of questions completed by one 
                        questionsFinished += 1 
                        questionAnswered = True # Sets the current question to having been answered
            
            if page == "Settings": # The clicking logic if the user is on the settings page
                detection = settings.detectClick(mousePos) # Checks what the user clicked on
                if detection != "NONE": # Runs if the next button was clicked
                    questionType = detection[0] # Sets the question and answer types for the quiz
                    answerType = detection[1]
                    question.newQuestion(questionType, answerType, qs.questionsDict, questionsFinished) # Generates a question to start the quiz with
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