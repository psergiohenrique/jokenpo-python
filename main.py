################# IMPORT LIBS AND INIT #################
import pygame
from pygame import mixer
from time import sleep
from random import randint
from pygame.locals import *
import sys
print(sys.path)

pygame.init()
mixer.init()
################# IMPORT LIBS AND INIT #################

################# CONFIG SCREEN #################
width_screen = 780
height_screen = 580
screenGame = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption('jokenpo - Paradigmas com Python')
################# CONFIG SCREEN #################

################# CONFIG GLOBAL VARIABLES #################
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
grey = (235, 235, 235)
numWins = 0
numDefeats = 0
numDraws = 0
################# CONFIG GLOBAL VARIABLES #################

################# IMPORT MEDIA #################
rockImage = pygame.image.load('images/rock.png').convert_alpha()
image_rock = pygame.transform.scale(rockImage, (300, 200))

imagePaper = pygame.image.load('images/paper.png').convert_alpha()
image_paper = pygame.transform.scale(imagePaper, (300, 200))

imageScissor = pygame.image.load('images/scissor.png').convert_alpha()
image_scissor = pygame.transform.scale(imageScissor, (300, 200))


mixer.music.load('media/song.mp3')
mixer.music.play(-1)
################# IMPORT MEDIA #################

################# FUNCTIONS TO USE BUTTONS AND TEXTS  #################


def printText(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def sumValue(type):
    if type == 'VENCEU':
        numWins += 1
    elif type == 'EMPATOU':
        numDraws += 1
    else:
        numDefeats += 1


def rockButton(x, y, width, height, action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screenGame, grey, (x, y, width, height+5))
        if click[0] == 1 and action != None:
            if action == 'PEDRA':
                rockChoice()

    screenGame.blit(image_rock, (x, y, width, height))


def paperButton(x, y, width, height, action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screenGame, grey, (x, y, width, height+5))
        if click[0] == 1 and action != None:
            if action == 'PAPEL':
                paperChoice()

    screenGame.blit(image_paper, (x, y, width, height))


def scissorButton(x, y, width, height, action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screenGame, grey, (x, y, width, height+5))
        if click[0] == 1 and action != None:
            if action == 'TESOURA':
                scissorChoice()

    screenGame.blit(image_scissor, (x, y, width, height))
################# FUNCTIONS TO USE BUTTONS AND TEXTS  #################


################# CHOOSE BUTTONS  #################
def screenGameChoice():

    getOut = False

    while not getOut:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()

        screenGame.fill(white)

        rockButton(15, 5, 300, 200, 'PEDRA')
        paperButton(400, 5, 300, 200, 'PAPEL')
        scissorButton(15, 250, 300, 200, 'TESOURA')

        backButton('Voltar', 450, 310, 100, 50, (0, 0, 200), blue, 'Voltar')

        font = pygame.font.Font('freesansbold.ttf', 20)
        text_wins, rect = printText('VITORIAS: ' + str(numWins), font)
        text_draws, rect = printText('EMPATES: ' + str(numDraws), font)
        text_defeats, rect = printText('DERROTAS: ' + str(numDefeats), font)
        screenGame.blit(text_wins, (370, 400))
        screenGame.blit(text_draws, (370, 420))
        screenGame.blit(text_defeats, (370, 440))

        pygame.display.update()

    pygame.quit()
    quit()
################# CHOOSE BUTTONS  #################

################# RESULT WHEN THE CHOICE IS ROCK  #################


def rockChoice():
    choiceIA = randint(0, 2)

    getOut = False

    while not getOut:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()

        screenGame.fill(white)

        textToPrint = pygame.font.Font('freesansbold.ttf', 30)
        printThisText = textToPrint.render('Voce:', True, black)
        screenGame.blit(printThisText, (40, 60))

        textToPrint = pygame.font.Font('freesansbold.ttf', 30)
        printThisText = textToPrint.render('Bot:', True, black)
        screenGame.blit(printThisText, (40, 420))

        screenGame.blit(image_rock, (200, 5))
        if choiceIA == 0:
            textToPrint = pygame.font.Font('freesansbold.ttf', 30)
            printThisText = textToPrint.render('EMPATE', True, black)
            screenGame.blit(printThisText, (300, 250))
            screenGame.blit(image_rock, (200, 340))

        elif choiceIA == 1:
            textToPrint = pygame.font.Font('freesansbold.ttf', 30)
            printThisText = textToPrint.render('PERDEU', True, red)
            screenGame.blit(printThisText, (300, 250))
            screenGame.blit(image_paper, (200, 340))

        elif choiceIA == 2:
            textToPrint = pygame.font.Font('freesansbold.ttf', 30)
            printThisText = textToPrint.render('VENCEU', True, green)
            screenGame.blit(printThisText, (300, 250))
            screenGame.blit(image_scissor, (200, 340))

        pygame.display.update()
        sleep(2)
        screenGameChoice()
################# RESULT WHEN THE CHOICE IS ROCK  #################


################# RESULT WHEN THE CHOICE IS PAPER  #################
def paperChoice():

    choiceIA = randint(0, 2)

    getOut = False

    while not getOut:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()

        screenGame.fill(white)

        textToPrint = pygame.font.Font('freesansbold.ttf', 30)
        printThisText = textToPrint.render('Voce:', True, black)
        screenGame.blit(printThisText, (40, 60))

        textToPrint = pygame.font.Font('freesansbold.ttf', 30)
        printThisText = textToPrint.render('Bot:', True, black)
        screenGame.blit(printThisText, (40, 420))

        screenGame.blit(image_paper, (200, 5))

        if choiceIA == 0:
            textToPrint = pygame.font.Font('freesansbold.ttf', 30)
            printThisText = textToPrint.render('VENCEU', True, green)
            screenGame.blit(printThisText, (300, 250))
            screenGame.blit(image_rock, (200, 340))

        elif choiceIA == 1:
            textToPrint = pygame.font.Font('freesansbold.ttf', 30)
            printThisText = textToPrint.render('EMPATE', True, black)
            screenGame.blit(printThisText, (300, 250))
            screenGame.blit(image_paper, (200, 340))

        elif choiceIA == 2:
            textToPrint = pygame.font.Font('freesansbold.ttf', 30)
            printThisText = textToPrint.render('PERDEU', True, red)
            screenGame.blit(printThisText, (300, 250))
            screenGame.blit(image_scissor, (200, 340))

        pygame.display.update()
        sleep(2)
        screenGameChoice()
################# RESULT WHEN THE CHOICE IS PAPER  #################


################# RESULT WHEN THE CHOICE IS SCISSOR  #################


def scissorChoice():

    choiceIA = randint(0, 2)

    getOut = False

    while not getOut:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()

        screenGame.fill(white)

        textToPrint = pygame.font.Font('freesansbold.ttf', 30)
        printThisText = textToPrint.render('Voce:', True, black)
        screenGame.blit(printThisText, (40, 60))

        textToPrint = pygame.font.Font('freesansbold.ttf', 30)
        printThisText = textToPrint.render('Bot:', True, black)
        screenGame.blit(printThisText, (40, 420))

        screenGame.blit(image_scissor, (200, 5))
        if choiceIA == 0:
            textToPrint = pygame.font.Font('freesansbold.ttf', 30)
            printThisText = textToPrint.render('PERDEU', True, red)
            screenGame.blit(printThisText, (300, 250))
            screenGame.blit(image_rock, (200, 340))

        elif choiceIA == 1:
            textToPrint = pygame.font.Font('freesansbold.ttf', 30)
            printThisText = textToPrint.render('VENCEU', True, green)
            screenGame.blit(printThisText, (300, 250))
            screenGame.blit(image_paper, (200, 340))

        elif choiceIA == 2:
            textToPrint = pygame.font.Font('freesansbold.ttf', 30)
            printThisText = textToPrint.render('EMPATE', True, black)
            screenGame.blit(printThisText, (300, 250))
            screenGame.blit(image_scissor, (200, 340))

        pygame.display.update()
        sleep(2)
        screenGameChoice()
################# RESULT WHEN THE CHOICE IS SCISSOR  ################


################# BUTTONS PLAY AND BACK  ################
def backButton(msg, x, y, width, height, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screenGame, ac, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == 'Voltar':
                screenGameDashboard()

    else:
        pygame.draw.rect(screenGame, ic, (x, y, width, height))

    textToPrint = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = printText(msg, textToPrint)
    TextRect.center = ((x+(width/2), (y+(height/2))))
    screenGame.blit(TextSurf, TextRect)


def button(msg, x, y, width, height, ic, ac, action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screenGame, ac, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == 'Jogar':
                screenGameChoice()
            elif action == 'Sair':
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(screenGame, ic, (x, y, width, height))

    textToPrint = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = printText(msg, textToPrint)
    TextRect.center = ((x+(width/2), (y+(height/2))))
    screenGame.blit(TextSurf, TextRect)
################# BUTTONS PLAY AND BACK  ################


################# FIRST SCREEN ################
def screenGameDashboard():

    getOut = False

    while not getOut:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        screenGame.fill(white)

        largeText = pygame.font.Font('freesansbold.ttf', 35)
        TextSurf, TextRect = printText(
            'jokenpo - Paradigmas com Python', largeText)
        TextRect.center = ((width_screen/2), (height_screen/2))
        screenGame.blit(TextSurf, TextRect)

        button('Jogar', 100, 400, 100, 50, (0, 200, 0), green, 'Jogar')
        button('Sair', 500, 400, 100, 50, (200, 0, 0), red, 'Sair')

        pygame.display.update()
################# FIRST SCREEN ################


################# DEFAULT FUNCTIONS ################
screenGameDashboard()
pygame.quit()
quit()
