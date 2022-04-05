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

    def __init__(self, label, font, backingColour, tColour, screen):
        self.selected = 0
        self.__label = font.render(label, False, tColour)
        self.__backdrop = backingColour
        self.__screen = screen
        self.text = label


    def draw(self, x, y):
        topLeftX = (self.__screen.get_width()/4)*(x + 1) # Finds the top left x of the given button
        topLeftY = self.__screen.get_height() - (self.__screen.get_height()/5)*(y+1) # Finds the top left y of the given button

        self.__coords = (topLeftX, topLeftY)
        if self.selected == 1: # Checks if the button is selected
            selecColour = (self.__backdrop[0] + 10, self.__backdrop[1] + 10, self.__backdrop[2] + 10)
            pygame.draw.rect(self.__screen, selecColour, (topLeftX - 5, topLeftY - 5, xSize, ySize), 0, -1, 50, 50, 50, 50) # Draws a rectangle for the button to be on
        elif self.selected == 0:
            pygame.draw.rect(self.__screen, self.__backdrop, (topLeftX - 5, topLeftY - 5, xSize, ySize), 0, -1, 50, 50, 50, 50) # Draws a rectangle for the button to be on
        self.__screen.blit(self.__label, (topLeftX, topLeftY))
    
    def clickDetection(self, mousePos):
        if mousePos[0] > self.__coords[0] and mousePos[0] < self.__coords[0] + self.__label.get_width() + 10:
            if mousePos[1] > self.__coords[1] and mousePos[1] < self.__coords[1] + self.__label.get_height() + 10:
                return True


buttons = np.array([[Button for y in range (3)] for x in range(2)]) # An array ot store the answer buttons in
labels = ["Capital", "Flag", "Location"] # The labels for the buttons
global nextButton
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
    pygame.draw.rect(screen, backColour, (screen.get_width()/2 - settingsTitle.get_width()/2, 25, screen.get_width()/4 + settingsTitle.get_width()/2, 25 + settingsTitle.get_height()), 0, -1, 100, 100, 100, 100) # Draws a rect for the title to go onto
    screen.blit(settingsTitle, ((screen.get_width()/2 - settingsTitle.get_width()/2) + 2, 26)) # Writes the title on top of the rectangle

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
                else:
                    for i in range(3):
                        buttons[x, i].selected = 0
                    for j in range(2):
                        buttons[j, y].selected = 0
                    buttons[x, y].selected = 1
    return "NONE"