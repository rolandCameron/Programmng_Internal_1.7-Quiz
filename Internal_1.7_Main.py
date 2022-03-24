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

# An array with all the settings buttons in it
settingsButtons = np.array([[Fonts.TITLE_F.render('Location', False, (Colours.TEXT_C)), Fonts.TITLE_F.render('Flag', False, (Colours.TEXT_C)), Fonts.TITLE_F.render('Capital', False, (Colours.TEXT_C))], [Fonts.TITLE_F.render('Location', False, (Colours.TEXT_C)), Fonts.TITLE_F.render('Flag', False, (Colours.TEXT_C)), Fonts.TITLE_F.render('Capital', False, (Colours.TEXT_C))]])

#FUNCTIONS

#MAIN
while True:
    screen.fill(Colours.BACKGROUND_C) # Initialises the screen as the background colour

    if page == "Settings":
        # Draws a rectangle behind the title
        pygame.draw.rect(screen, Colours.QUESTION_C, (screen.get_width()/2 - settingsTitle.get_width()/2, 25, screen.get_width()/4 + settingsTitle.get_width()/2, 25 + settingsTitle.get_height()), 0, -1, 100, 100, 100, 100) 
        screen.blit(settingsTitle, ((screen.get_width()/2 - settingsTitle.get_width()/2) + 2, 26)) # Writes the title on top of the rectangle

        for y in range(3): 
            for x in range(2):
                topLeftX = (screen.get_width()/4)*(x + 1)
                topLeftY = screen.get_height() - (screen.get_height()/4)*(y+1)
                pygame.draw.rect(screen, Colours.QUESTION_C, (topLeftX, topLeftY, settingsButtons[x, y].get_width() + 10, settingsButtons[x, y].get_height() + 10), 0, -1, 50, 50, 50, 50)
                screen.blit(settingsButtons[x, y], (topLeftX, topLeftY))

    for event in pygame.event.get(): # Runs for each possible event in pygame
        if event.type == pygame.QUIT:
            pygame.quit() # Closes the window
            sys.exit() # Ends the program

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