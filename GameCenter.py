import pygame
from pygame.locals import *
from random import *
from time import *
from gameModule import *
pygame.init()
screen=pygame.display.set_mode((900,600))
pygame.display.set_caption('Games Menu')
def show_text(msg,x,y,color,size):
    fontobj=pygame.font.SysFont("freesans",size,False,False)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
b1=0
b2=0
green=(0,200,10)
red=(200,10,0)
while True:	
    screen.fill([0,0,0])
    sleep(.01)
    pygame.draw.rect(screen, green,(35,25,250,100))
    show_text("Tic Tac Toe",35,45,(250,255,255), 51)
    
    pygame.draw.rect(screen,green,(315,25,250,100))
    show_text("Flappy Bird",315,45,(255,255,255), 50)

    pygame.draw.rect(screen,green,(595,25,250,100))
    show_text("Tiles",625,25,(255,255,255), 90)
    
    pygame.draw.rect(screen, green,(35,175,250,100))
    show_text("Snake",55,185,(250,255,255), 70)
    
    pygame.draw.rect(screen,green,(315,175,250,100))
    show_text("Pong",355,185,(255,255,255), 70)

    pygame.draw.rect(screen,green,(35,325,250,100))
    show_text("Hangman",35,335,(255,255,255), 58)

    pygame.draw.rect(screen,green,(315,325,250,100))
    show_text("Balloon",330,335,(255,255,255), 70)

    pygame.draw.rect(screen,green,(35,475,250,100))
    show_text("Ninja",50,475,(255,255,255), 90)

    pygame.draw.rect(screen,red,(315,475,250,100))
    show_text("Quit",330,475,(255,255,255), 100)

    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            if 35<event.pos[0]<285 and 25<event.pos[1]<125:
                screen.fill([0,0,0])
                TTT()
                sleep(1)
            elif 315<event.pos[0]<565 and 25<event.pos[1]<125:
                screen.fill([0,0,0])
                FB()
                sleep(1)
            elif 595<event.pos[0]<845 and 25<event.pos[1]<125:
                screen.fill([0,0,0])
                Tiles()
                sleep(1)
            elif 35<event.pos[0]<285 and 175<event.pos[1]<275:
                screen.fill([0,0,0])
                Snake()
                sleep(1)
            elif 315<event.pos[0]<565 and 175<event.pos[1]<275:
                screen.fill([0,0,0])
                Pong()
                sleep(1)
            elif 35<event.pos[0]<285 and 325<event.pos[1]<425:
                screen.fill([0,0,0])
                Hangman()
                sleep(1)
            elif 315<event.pos[0]<565 and 325<event.pos[1]<425:
                screen.fill([0,0,0])
                Balloon()
                sleep(1)
            elif 35<event.pos[0]<285 and 475<event.pos[1]<575:
                screen.fill([0,0,0])
                Ninja()
                sleep(1)
            elif 315<event.pos[0]<565 and 475<event.pos[1]<575:
                pygame.quit()
                exit()
            screen=pygame.display.set_mode((900,600))
            pygame.display.set_caption('Games Menu')
        if event.type==QUIT:
            pygame.quit()
            exit()
    pygame.display.update()