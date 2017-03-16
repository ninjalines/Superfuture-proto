#!/usr/bin/env python

from Constants import *
from Game import game, console
import pygame

class Pygame(object):
	def __init__(self, ):
		self.pg = pygame
		self.displayInit()
		self.fontInit()
		self.mixerInit()
	def displayInit(self, ):
		if not self.pg.display.get_init():
			self.pg.display.init()
			if self.pg.display.get_init():
				print 'The display module initialized successfully.'
			else:
				print 'The display module for pygame would not initialize.'
				game.quit()
	def fontInit(self, ):
		if not self.pg.font.get_init():
			self.pg.font.init()
			if self.pg.font.get_init():
				print 'The font module initialized successfully.'
			else:
				print 'The font module for pygame would not initialize.'
				game.quit()
	def mixerInit(self, ):
		if not self.pg.mixer.get_init():
			self.pg.mixer.init()
			if self.pg.mixer.get_init():
				print 'The mixer module initialized successfully.'
			else:
				print 'The mixer module for pygame would not initialize.'
				game.quit()
class Display(object):
	DISPLAY = DISPLAY
	def __init__(self, ):
		self.identification = self.returnIdentification()
		pygame.display.set_mode((screenSize))
		self.display = pygame.display.get_surface()
		self.displaySize = self.display.get_size()
		self.displayRect = self.display.get_rect()
		self.NAME = 'DISPLAY'
		self.image = self.display
	def returnIdentification(self, ):
		identification = 'DISPLAY'
		return identification
	def returnName(self, ):
		return self.NAME
	def returnDisplay(self, ):
		return self.display

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
	def __init__(self, ):
		self.display = pygame.display.get_surface()

	def drawToScreen(self, item):
		self.display.blit(item.image, item.pos)

	def update(self, ):
		#this line is used in case the display surface resizes or changes.
		self.display = pygame.display.get_surface()
		#This draws certain things to the screen.
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


"""This is to have a 'room' that will act as a holding place for objects."""
class Chamber(object):
	def __init__(self, empty=None, *args):
		self.objects = {'DISPLAY':None, 'CONSOLE':None, 'PLAYERS':[]}
		self.write = {'DISPLAY':False, 'CONSOLE':False, 'PLAYERS':[]}
		if args:
			for i in args:
				self.objects[i.identification] = i.image
				
				
	def __len__(self, ):
		return len(self.big)
	def __getitem__(self, key):
		return self.big[key]
	def __setitem__(self, key, value):
		self.big[key] = value
	def __delitem__(self, key):
		del self.big[key]
	def __iter__(self,):
		return iter(self.big)
	def setObject(self, name, Object):
		self.objects[name] = Object
	def setValidity(self, name, validity):
		self.write[name] = validity
	def resetValidity(self, name=none, *names):
		if names:
			for i in names[0]:
				self.write[i] = False
		else:
			self.write[name] = False
	def returnObject(self, name):
		return self.objects[name]
	def returnValidity(self, name):
		return self.write[name]
	def setObjectAndValidity(self, name, obj, validity):
		self.objects[name], self.write[name] = obj, validity

