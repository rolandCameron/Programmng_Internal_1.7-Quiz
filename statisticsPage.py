# This file contains the code for the statistics page at the end of the quiz
# Code in here will be called in "Internal_1.7_Main.py"

import pygame

xSize = 200
ySize = 50

def showStatistics(totalQ, numCorr, bColour, tColour, font, screen):
    labels = [font.render(f"You scored {numCorr}/{totalQ}, or", False, tColour), font.render(f"{(numCorr/totalQ)*100}%", False, tColour)]
    for y in range(2):
        topLeftX = (screen.get_width()/20)*(8) # Finds the top left x of the given text box
        topLeftY = screen.get_height() - (screen.get_height()/6)*(5-y) # Finds the top left y of the given text box

        pygame.draw.rect(screen, bColour, (topLeftX - (xSize/2), topLeftY - (ySize/2), xSize*3, ySize*3), 0, -1, 50, 50, 50, 50)
        screen.blit(labels[y], (topLeftX, topLeftY))

def showButtons(bColour, tColour, font, screen):
    labels = [font.render("Same Quiz?", False, tColour), font.render("Settings Page?", False, tColour), font.render("Quit?", False, tColour)]
    for y in range(3):
        topLeftX = (screen.get_width()/20)*(8) # Finds the top left x of the given button
        topLeftY = screen.get_height() - (screen.get_height()/6)*(5-(y + 2)) # Finds the top left y of the given button

        pygame.draw.rect(screen, bColour, (topLeftX - (xSize/2), topLeftY - (ySize/2), xSize*3, ySize*3), 0, -1, 50, 50, 50, 50)
        screen.blit(labels[y], (topLeftX, topLeftY))

def detectClick(mousePos, screen):
    for y in range(3):
        topLeftX = (screen.get_width()/20)*(8) # Finds the top left x of the given button
        topLeftY = screen.get_height() - (screen.get_height()/6)*(5-(y + 2)) # Finds the top left y of the given button

        if mousePos[0] > (topLeftX - (xSize/2)) and mousePos[0] < (topLeftX + xSize*3):
            if mousePos[1] > (topLeftY - (ySize/2)) and mousePos[1] < (topLeftY + ySize*3):
                return y
        else:
            return "No Click"