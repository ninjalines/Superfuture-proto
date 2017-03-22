#!/usr/bin/env python

from Constants import *

import pygame

def findBiggest(*args):
	array = []
	for i in Alphabet:
		size = CharacterBuffer.returnSizeOfText(i)
		if size not in array:
			array.append(size)

	for i in range(len(array)):
		

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
	def __init__(self, ):
		self.identification = self.returnIdentification()
		pygame.display.set_mode((screenSize), RESIZABLE)
		self.display = pygame.display.get_surface()
		self.displaySize = self.display.get_size()
		self.displayRect = self.display.get_rect()
		self.NAME = DISPLAY
		self.image = self.display
		self.position = 0, 0
		self.identification = self.returnIdentification()
	def returnIdentification(self, ):
		identification = DISPLAY
		return identification
	def returnName(self, ):
		return self.NAME
	def returnDisplay(self, ):
		return self.display

	def getId(self, ):
		return self.ident
	def updateScreen(self, chamber, size):
		self.display = pygame.display.set_mode(size, RESIZABLE)
		self.displaySize = self.display.get_size()
		self.displayRect = self.display.get_rect()
		self.image = self.display
		chamber.items[DISPLAY] = self

	def getRect(self, ):
		return self.displayRect

	def getSize(self, ):
		return self.displaySize

class DrawStack(object):
	def __init__(self, ):
		self.display = pygame.display.get_surface()
		self.chambers = {}

	#adds Chamber() to self.chambers dict
	def addChamber(self, chamber=None, *chambers):
		if chambers:
			if isinstance(chambers[0], (list, tuple)):
				for chamberList in chambers:
					for chamber in chamberList:
						self.chambers[chamber.identification] = chamber
			elif chambers:
				for chamber in chambers:
					self.chambers[chamber.identification] = chamber
		if chamber:
			self.chambers[chamber.identification] = chamber

	def doesChamberExist(self, identification ):
		if self.chambers.has_key(identification):
			return True
		elif not self.chambers.has_key(identification):
			return False

	def drawToScreen(self, item):
		self.display.blit(item.image, item.position)
	#checks if chambers objects are ready to be written and writes them to the screen
	#they are
	def update(self, ):
		if self.chambers:
			for key, chamber in self.chambers.iteritems():
				for key2, item in chamber.iteritems():
					if isinstance(item, (list, tuple)):
						counter = 0
						for listItem in chamber.write[key2]:
							if listItem:
								self.drawToScreen(item.items[key][counter])
							counter += 1

					elif chamber.write[key2]:
						self.drawToScreen(chamber.items[key2])

	#returns a Boolean value based on rather a chamber's item is ready to be blitted.
	def isActive(self, chamberIdentification, identification, identificationNumber=None):
		if self.chambers:
			for key, chamber in self.chambers.iteritems():
				if self.doesChamberExist(chamberIdentification):
					if isinstance(chamber.write[identification], (list, tuple)):
						if chamber.write[identification][identificationNumber]:
							return True
						else:
							return False
					elif chamber.write[identification]:
						return True
					else:
						return False
		else:
			return False
	
	def add(self, theType, item):
		pass


"""This is to have a 'room' that will act as a holding place for objects."""
class Chamber(object):
	def __init__(self, identification=None, item=None, *args):
		self.items = {'DISPLAY':None, 'CONSOLE':None, 'PLAYERS':[]}
		self.write = {'DISPLAY':False, 'CONSOLE':False, 'PLAYERS':[]}
		if args:
			if isinstance(args[0], (list, tuple)):
				for tupleOrList in args:
					for item in tupleOrList:
						self.items[item.identification] = item
			else:
				for item in args:
					self.items[item.identification] = item
		elif item:
			self.items[item.identification] = item
		self.identification = identification
	def __len__(self, ):
		return len(self.items)
	def __getitem__(self, key):
		return self.items[key]
	def __setitem__(self, key, value):
		self.items[key] = value
	def __delitem__(self, key):
		del self.items[key]
	def __iter__(self,):
		return iter(self.objects)
	def setItem(self, name, Object):
		self.items[name] = Object
	def setValidity(self, name, validity):
		self.write[name] = validity
	def resetValidity(self, name=None, *names):
		if names:
			for i in names[0]:
				self.write[i] = False
		else:
			self.write[name] = False
	def returnItem(self, name):
		return self.items[name]
	def returnValidity(self, name):
		return self.write[name]
	def setItemAndValidity(self, name, item, validity):
		self.items[name], self.write[name] = item, validity
	def iteritems(self, ):
		return self.items.iteritems()

class CharacterBuffer(object):
	charBuffers = []
	characterFont = pygame.font.SysFont('ubuntumono', 10)
	consolePresent = False
	def __init__(self, char):
		CharacterBuffer.append(self)
		self.image = CharacterBuffer.charFont.render(char, True, WHITE, None)
	@staticmethod
	def returnSizeOfText(char):
		return CharacterBuffer.charFont.size(char)
	@staticmethod
	def resizeText(size):
		CharacterBuffer.characterFont = pygame.font.SysFont('ubuntumono', size)


