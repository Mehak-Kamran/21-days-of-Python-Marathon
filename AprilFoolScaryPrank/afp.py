#import pygame 
import pygame
from time import sleep

#initialize pygame
pygame.init()
#creating window/screen
screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)#since i want to use whole screen
#playing and loading sound
pygame.mixer.init()
pygame.mixer.music.load("AprilFoolScaryPrank/ratsasan.mp3")
pygame.mixer.music.play()
sleep(3)
#playing again
pygame.mixer.music.load("AprilFoolScaryPrank/scary.mp3")
pygame.mixer.music.play()
sleep(2)
#loading img
photo=pygame.image.load("AprilFoolScaryPrank/scr.jpg")
screen.blit(photo,(0,0))
pygame.display.update()
sleep(3)