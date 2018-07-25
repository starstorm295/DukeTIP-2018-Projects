import os
import random
import pygame
import math
import sys

number = None
running = 1

boxWidth = 110
boxHeight = 110
boxX = 340
boxY = 200

white = (255,255,255)

pygame.init()

responses = ["Sit on it some more.", "Concentrate and ask again", "Response hazy, try again", "That sounds best",  "My sources say no", "Are you sure?", "What does your heart say?"]
WHITE = (0, 255,0)
screen_width = 820
screen_height =  480
msg = "click for an answer"

bkrnd_img = "img/ballbg.png"


screen = pygame.display.set_mode((screen_width,screen_height), 0, 32) # Resolution == width and height
pygame.display.set_caption("Magic 8 Button")
mouse_pos = pygame.mouse.get_pos()

mainButton = pygame.Rect(0, 0 ,50, 50)
mouse_pos = pygame.mouse.get_pos()

background = pygame.image.load(bkrnd_img).convert()


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def ShowMessage(text,x,y):
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ( (x+(boxWidth/2) + 25), (y+(boxHeight/2) + 70) )
    screen.blit(textSurf, textRect)

def button(text,x,y):
    global number
    global msg
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(screen, (0,162,232),(boxX,boxY,boxWidth,boxHeight))
    if x + boxWidth > mouse[0] > x and y+boxHeight > mouse[1] > y:
        if click[0] == 1:
            screen.blit(background, (0,0))
            print("this happened")
            number = random.randint(0,6)

while running:
    done = False   #quitting the game code
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.blit(background, (0,0))
    button("test",boxX,boxY)
    if(number != None):
        msg = str(responses[number])
    print(number)

    print(msg)
    ShowMessage(msg,315,120)
    pygame.display.update()
    pygame.display.flip() ##refresh the screen
