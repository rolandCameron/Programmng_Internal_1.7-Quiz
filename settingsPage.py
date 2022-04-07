# This file contains the code for the settings page
# Code in here will be called in "Internal_1.7_Main.py"

# IMPORTS
from ast import Global
from turtle import Screen
import pygame
import numpy as np

# VARIABLES
xSize = 250
ySize = 60


class Button:
    __label = "" # Carries the buttons label object
    __backdrop = () # A tuple that carries the background colour of the button
    __screen = "NONE ASSIGNED" # Will carry the screen object to be printed on to
    __coords = (0, 0) # Tuple for storing the buttons location on any given frame

    selected = 0 # A boolean of the buttons selection status
    text = "" # Carries the buttons text

    def __init__(self, label, font, backingColour, tColour, screen): # Sets all the parameters for the button
        self.selected = 0
        self.__label = font.render(label, False, tColour)
        self.__backdrop = backingColour
        self.__screen = screen
        self.text = label


    def draw(self, x, y):
        topLeftX = (self.__screen.get_width()/4)*(x + 1) # Finds the top left x of the given button
        topLeftY = self.__screen.get_height() - (self.__screen.get_height()/5)*(y+1) # Finds the top left y of the given button

        self.__coords = (topLeftX, topLeftY) # Changes the position of the buton so that it can later be used when detecting clicks
        if self.selected == 1: # Checks if the button is selected
            selecColour = (self.__backdrop[0] - 1, self.__backdrop[1] - 40, self.__backdrop[2] - 40) # Defines the clour to be used while the button is selected
            pygame.draw.rect(self.__screen, selecColour, (topLeftX - (xSize/2), topLeftY - (ySize/2), xSize*1.5, ySize*1.5), 0, -1, 50, 50, 50, 50) # Draws a rectangle for the button to be on
        elif self.selected == 0:
            pygame.draw.rect(self.__screen, self.__backdrop, (topLeftX - (xSize/2), topLeftY - (ySize/2), xSize*1.5, ySize*1.5), 0, -1, 50, 50, 50, 50) # Draws a rectangle for the button to be on
        self.__screen.blit(self.__label, (topLeftX, topLeftY)) # Writes the actual text onto the screen
    
    def clickDetection(self, mousePos): # Detects if the button has been clicked
        if mousePos[0] > self.__coords[0] - (xSize/2) and mousePos[0] < self.__coords[0] + xSize*1.5: # Checks if the click was in the x range of the button
            if mousePos[1] > self.__coords[1] - (ySize/2) and mousePos[1] < self.__coords[1] + ySize*1.5: # Checks if the click was in the y range of the button
                return True


buttons = np.array([[Button for y in range (3)] for x in range(2)]) # An array to store the answer buttons in
labels = ["Capital", "Population", "Country"] # The labels for the buttons
global nextButton # Initialises the next button
nextButton = Button

# FUNCTIONS
def initButtons(font, colour, tColour, screen): # Initialises the buttons
    global nextButton
    nextButton = Button("Next?", font, colour, tColour, screen) # Initialises a "next" button
    for y in range(3): # Runs for each possible answer - question types
        for x in range(2): # Runs for the two columns
            buttons[x, y] = Button(labels[y], font, colour, tColour, screen) # Adds the buttons to the aforementioned array

def showTitle(screen, font, fontColour, backColour): # A function to show the title for the settings page
    settingsTitle = font.render('Select your question and answer types', False, (fontColour)) # The settings title
    pygame.draw.rect(screen, backColour, (screen.get_width()/2 - xSize*2, 25, xSize*4, ySize*2), 0, -1, 100, 100, 100, 100) # Draws a rect for the title to go onto
    screen.blit(settingsTitle, ((screen.get_width()/2 - settingsTitle.get_width()/2) + 2, 26)) # Writes the title on top of the rectangle

    columnTitle = [font.render('Question:', False, (fontColour)), font.render('Answer:', False, (fontColour))]
    for x in range(2):
        topLeftX = (screen.get_width()/4)*(x + 1) # Finds the top left x of the given button
        topLeftY = screen.get_height() - (screen.get_height()/5)*(4)

        pygame.draw.rect(screen, backColour, (topLeftX - xSize/2, topLeftY - ySize/2, xSize*1.5, ySize*2), 0, -1, 50, 50, 50, 50) # Draws a rect for the title to go onto
        screen.blit(columnTitle[x], (topLeftX, topLeftY))

def printButtons(): # A function to print the settings buttons
    for y in range(3): # Runs for each possible answer - question types
        for x in range(2): # Runs for the two columns
            buttons[x, y].draw(x, y) # Uses the draw function in the given button
    nextButton.draw(2, 3)

def detectClick(mousePos):
    numSelected = 0
    selectedLabels = []
    if nextButton.clickDetection(mousePos):
        for x in range(2): # Runs for each column
            for y in range(3): # Runs for each possible answer - question types
                if buttons[x, y].selected == 1:
                    numSelected += 1
                    selectedLabels.append(buttons[x, y].text)
        if numSelected == 2:
            return selectedLabels
    for y in range(3): # Runs for each possible answer - question types
        for x in range(2): # Runs for the two columns
            if buttons[x, y].clickDetection(mousePos): # Checks for a click on the given button 
                if buttons[x, y].selected == 1:
                    buttons[x, y].selected = 0
                else: # Deselcts all the other button in its row and column. This prevents duplicate answers
                    for i in range(3):
                        buttons[x, i].selected = 0
                    for j in range(2):
                        buttons[j, y].selected = 0
                    buttons[x, y].selected = 1
    return "NONE"