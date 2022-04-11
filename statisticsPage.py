# This file contains the code for the statistics page at the end of the quiz
# Code in here will be called in "Internal_1.7_Main.py"

# IMPORTS
import pygame

# VARIABLES
xSize = 200 # x size of buttons
ySize = 50 # y size of buttons

def showStatistics(totalQ, numCorr, bColour, tColour, font, screen): # Shows all the statistics
    labels = [font.render(f"You scored {numCorr}/{totalQ}, or", False, tColour), font.render(f"{(numCorr/totalQ)*100}%", False, tColour)] # A list containing the fraction and percentage score of the player
    for y in range(2): # Runs for the two statistics
        topLeftX = (screen.get_width()/20)*(8) # Finds the top left x of the statistics text boxes
        topLeftY = screen.get_height() - (screen.get_height()/6)*(5-y) # Finds the top left y of the given text box

        pygame.draw.rect(screen, bColour, (topLeftX - (xSize/2), topLeftY - (ySize/2), xSize*3, ySize*3), 0, -1, 50, 50, 50, 50) # Draws a rectangle behind the statistics text
        screen.blit(labels[y], (topLeftX, topLeftY)) # Writes the text onto the screen

def showButtons(bColour, tColour, font, screen): # Shows the buttons on the statistics page
    labels = [font.render("Same Quiz", False, tColour), font.render("Settings Page", False, tColour), font.render("Quit", False, tColour)] # Creates a list of the button labels
    for y in range(3): # Runs for each button
        topLeftX = (screen.get_width()/20)*(8) # Finds the top left x of the buttons
        topLeftY = screen.get_height() - (screen.get_height()/6)*(5-(y + 2)) # Finds the top left y of the given button

        pygame.draw.rect(screen, bColour, (topLeftX - (xSize/2), topLeftY - (ySize/2), xSize*3, ySize*3), 0, -1, 50, 50, 50, 50) # Draws a rectangle behind the buttons
        screen.blit(labels[y], (topLeftX, topLeftY)) # Writes the button labels onto the screen

def detectClick(mousePos, screen): # Checks what was clicked
    for y in range(3): # Runs for each button
        topLeftX = (screen.get_width()/20)*(8) # Finds the top left x of the buttons
        topLeftY = screen.get_height() - (screen.get_height()/6)*(5-(y + 2)) # Finds the top left y of the given button

        if mousePos[0] > (topLeftX - (xSize/2)) and mousePos[0] < (topLeftX + xSize*3): # Checks the click was inside the x and y of the button
            if mousePos[1] > (topLeftY - (ySize/2)) and mousePos[1] < (topLeftY + ySize*3):
                return y # Returns the button

        return "No Click" # Returns if the user didn't click on a button