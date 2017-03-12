#!/usr/bin/env python

import Constants
from Constants import display
import pygame
from pygame.locals import *
from Constants import *
textBoxSize = screenSize[0]*.8, screenSize[1]*.5 
textColor = pygame.Color(255, 0, 0, 50)

class Console(object):
	textBox = pygame.Surface(textBoxSize) 
	textBox.convert_alpha()
	textBox.fill(textColor)
	summon = K_BACKQUOTE
	def __init__(self, ):
		self.active = False
		self.updateStack = False

	def update(self,):
		if self.active:
			if self.updateStack:
				Game.drawStack.append(Console.textBox) #make an object to handle this.
		elif not self.active:
			if not self.updateStack:
				Game.drawStack.pop()
					
	def activate(self, ):
		print 'its updating.'
		if self.active:
			self.active = False
			self.updateStack = False
		elif not self.active:
			self.active = True
			self.updateStack = True

console = Console()
