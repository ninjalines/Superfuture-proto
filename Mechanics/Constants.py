#!/usr/bin/env python

import StartPygame
import pygame
from pygame.locals import *

#COLORS
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
BLUE = pygame.Color(0, 0, 255)
LIME = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
YELLOW = pygame.Color(255, 255, 0)
AQUA = pygame.Color(0, 255, 255)
SILVER = pygame.Color(192, 192, 192)
GRAY = pygame.Color(128, 128, 128)
MAROON = pygame.Color(128, 0, 0)
OLIVE = pygame.Color(128, 128, 0)
GREEN = pygame.Color(0, 128, 0)
PURPLE = pygame.Color(128, 0, 128)
TEAL = pygame.Color(0, 128, 128)
NAVY = pygame.Color(0, 0, 128)
CRIMSON = pygame.Color(220, 20, 60)

clock = pygame.time.Clock()
FPS = 120

DIRECTIONS = {'UP':0, 'DOWN':1, 'LEFT':2, 'RIGHT':3, 'UPLEFT':4, 'UPRIGHT':5, 'DOWNLEFT':6, 'DOWNRIGHT':7}
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
UPLEFT = 'UPLEFT'
UPRIGHT = 'UPRIGHT'
DOWNLEFT = 'DOWNLEFT'
DOWNRIGHT = 'DOWNRIGHT'

CONSOLE = 'CONSOLE'
DISPLAY = 'DISPLAY'
SPECIAL = 'SPECIAL'

screenSize = 800, 600
display = pygame.display.set_mode((800, 600), RESIZABLE)

def displayIsSet( ):
	if pygame.display.get_init():
		return True
	else:
		return False

def init():
	pygame.display.set_mode((800, 600), RESIZABLE)
