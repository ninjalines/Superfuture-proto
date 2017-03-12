#!/usr/bin/env python

from Constants import *
from Game import game, console

class Display(object):
	def __init__(self, ):
		self.display = pygame.display.get_surface()
		self.displaySize = self.display.get_size()
		self.displayRect = self.display.get_rect()
		self.ident = DISPLAY_ID
		
		self.image = self.display
	def getId(self, ):
		return self.ident
	def updateScreen(self, ):
		self.display = pygame.display.get_surface()
		self.displaySize = self.display.get_size()
		self.displayRect = self.display.get_rect()

	def getRect(self, ):
		return self.displayRect

	def getSize(self, ):
		return self.displaySize

class DrawStack(object):
	DISPLAY = [False]
	display = [None]
	SPECIAL = [False]*10
	special = [None]*10	
	master = {'DISPLAY':DrawStack.display, 'SPECIAL':DrawStack.special]
	MASTER = {'DISPLAY':DrawStack.DISPLAY, 'SPECIAL':DrawStack.SPECIAL]
	def __init__(self, ):
		self.x = 'hello'

	def drawToScreen(self, item):
		display.display.blit(item, item.location)

	def update(self, ):
		for specialDraw, drawTrue in zip(DrawStack.special, DrawStack.SPECIAL):
			if drawTrue:
				self.drawToScreen(specialDraw)
	#	for specialDraw, drawTrue in zip():
	#		pass

	def isActive(self, theType, item):
		if DrawStack.MASTER[theType][item.ident]:
			return True
		else:
			return False
	
	def add(self, theType, item):
		DrawStack.MASTER[theType][item.iD] = True
		DrawStack.master[theType][item.iD] = item.image



drawStack = DrawStack()

if displayIsSet():
	display = Display()
else:
	init()
	display = Display()
