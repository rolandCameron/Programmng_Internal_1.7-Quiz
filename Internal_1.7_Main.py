#IMPORTS
import pygame # Used for game window
import sys # Used to end program
import numpy as np

#INITIALIZATION
pygame.init() 

#CLASSES
class Colours: # Colours to be used within the project
    BACKGROUND_C = pygame.Color(1, 117, 15)
    TEXT_C = pygame.Color(0, 0, 0)
    QUESTION_C = pygame.Color(1, 51, 117, 125)
    QUESTION_SELECTED_C = pygame.Color(1, 51, 51, 125)

class Fonts: # Fonts to be used within the project
    TITLE_F = pygame.font.SysFont('Comic Sans MS', 50)
    QUESTION_F = pygame.font.SysFont('Comic Sans MS', 30)

#VARIABLES
monitorInfo = pygame.display.Info()
clock = pygame.time.Clock() # A clock that keeps track of game time
fps = 30 # The number of frames a second the game is running at
screen = pygame.display.set_mode((monitorInfo.current_w, monitorInfo.current_h - 20)) # The screen the game is drawn on to

page = "Settings" # The page displayed to the user

settingsTitle = Fonts.TITLE_F.render('Select your question and answer types', False, (Colours.TEXT_C)) # The settings title

nextText = Fonts.QUESTION_F.render('NEXT?', False, (Colours.TEXT_C)) # A text object with "NEXT?" inside it

# An array with all the settings buttons in it 
settingsButtons = np.array([[Fonts.QUESTION_F.render('Location', False, (Colours.TEXT_C)), Fonts.QUESTION_F.render('Flag', False, (Colours.TEXT_C)), Fonts.QUESTION_F.render('Capital', False, (Colours.TEXT_C))] for x in range(2)])
settingsButtonSelected = np.array([[0 for y in range(3)] for x in range(2)]) # Stores the colours of all the settings buttons

#FUNCTIONS

#MAIN
while True:
    screen.fill(Colours.BACKGROUND_C) # Initialises the screen as the background colour

    if page == "Settings":
        # Draws a rectangle behind the title
        pygame.draw.rect(screen, Colours.QUESTION_C, (screen.get_width()/2 - settingsTitle.get_width()/2, 25, screen.get_width()/4 + settingsTitle.get_width()/2, 25 + settingsTitle.get_height()), 0, -1, 100, 100, 100, 100) 
        screen.blit(settingsTitle, ((screen.get_width()/2 - settingsTitle.get_width()/2) + 2, 26)) # Writes the title on top of the rectangle

        nextTopLeftX = screen.get_width() - nextText.get_width() - 20
        nextTopLeftY = screen.get_height() - nextText.get_height() - 20
        pygame.draw.rect(screen, Colours.QUESTION_C, (nextTopLeftX, nextTopLeftY, nextText.get_width(), nextText.get_height()), 0, -1, 100, 100, 100, 100) # Draws the "NEXT" button
        screen.blit(nextText, (nextTopLeftX, nextTopLeftY)) # Writes the "NEXT" text

        for y in range(3): # Runs for each option available (Flag, Capital, Location)
            for x in range(2): # Runs for both columns
                topLeftX = (screen.get_width()/4)*(x + 1) # Finds the top left x of the given button
                topLeftY = screen.get_height() - (screen.get_height()/4)*(y+1) # Finds the top left y of the given button
                bColour = Colours.QUESTION_C # Resets the buttons colour

                if settingsButtonSelected[x, y] == 1: # Runs if the button is selected
                    bColour = Colours.QUESTION_SELECTED_C # Changes the buttons colour so that it shows the user it is selected

                pygame.draw.rect(screen, bColour, (topLeftX, topLeftY, settingsButtons[x, y].get_width() + 10, settingsButtons[x, y].get_height() + 10), 0, -1, 50, 50, 50, 50) # Draws a rectangle in this location
                screen.blit(settingsButtons[x, y], (topLeftX, topLeftY)) # Draws the text for the button

    for event in pygame.event.get(): # Runs for each possible event in pygame
        if event.type == pygame.QUIT:
            pygame.quit() # Closes the window
            sys.exit() # Ends the program
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos() # Gets the coordinates of the mouse pointer
            if page == "Settings":

                # This code checks if an answer/question button was clicked, runs for each button on the screen
                for y in range(3): # Runs for each option available (Flag, Capital, Location)
                    for x in range(2): # Runs for both columns
                        topLeftX = (screen.get_width()/4)*(x + 1) # Finds the top left x of the given button
                        topLeftY = screen.get_height() - (screen.get_height()/4)*(y+1) # Finds the top left y of the given button
                        if mousePos[0] > topLeftX and mousePos[0] < topLeftX + settingsButtons[x, y].get_width() + 10:
                            if mousePos[1] > topLeftY and mousePos[1] < topLeftY + settingsButtons[x, y].get_height() + 10:
                                if settingsButtonSelected[x, y] == 0: # Runs if the button isn't selected
                                    for i in range(3): # Runs for every button in the same column as the one selected
                                        settingsButtonSelected[x, i] = 0 # Deselects given button
                                    
                                    for j in range(2): # Makes sure the user hasn't selected a duplicate answer - question (eg. Capital - Capital, Flag - Flag...) 
                                        settingsButtonSelected[j, y] = 0 # Deselects given button

                                    settingsButtonSelected[x, y] = 1 # Changes the colour to let the user know it has been selected
                                else:
                                    settingsButtonSelected[x, y] = 0 # Deselects the button if it was already selected

                #This code checks if the next button was clicked
                if mousePos[0] < nextTopLeftX + nextText.get_height() and mousePos[0] > nextTopLeftX:
                    if mousePos[1] < nextTopLeftY + nextText.get_width() and mousePos[1] > nextTopLeftY:
                        page = "Config"
                        print(page)

    pygame.display.flip() # Updates the screen
    clock.tick(fps) # Waits for "fps" milliseconds

#DECOMPOSITION
"""
1. Present options for the topic of the quiz
    a. Create a pygame screen
    b. Present buttons for each of the answers and questions available (Flag - Capital, Capital - Flag, Country - Flag, etc...)
    c. Detect a click on these buttons
    d. Have the user confirm their selection, do not let them select the same answer and question eg. (flag - flag, capital - capital)

2. Allow users to choose the are they want to cover (eg. Asia, Africa, Europe), the number of questions they want to answer, and how they want to answer (Multiple choice, written response)
    a. Present a new screen of options, as detailed above
    b. Allow the user to select one option from each field (maybe multiple continents?)
    c. Allow the user to confirm their choices

3. Present questions one by one, with the desired answer option
    a. Present a question, with the related images
    b. Allow the user to answer in their chosen way
    c. Once they confirm their answer, move onto the next question

4. Once all the questions have been answered, give the user a score
    a. Present an end screen
    b. Show the user their score and percentage they got correct
    c. Display their answers, and which ones were correct

5. Ask if the user wants to do another quiz
    a. Allow the user to decide whether or not they want to play again
    b. Let them choose either the same quiz, or to change some of the parameters
"""