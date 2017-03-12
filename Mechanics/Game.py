#!/usr/bin/env python
"""Game.py"""
import Constants
from Constants import *
import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
class DrawStack(object):
	
	def __init__(self, ):
		self.stack = []
		
	def add(self, item):
		pass

	def add_list(self, itemList):
		pass



class Console(object):
	
	summon = K_BACKQUOTE
	font = pygame.font.SysFont('ubuntumono', 8, True, False)
	fontColor = RED
	
	widthPercentage = .8
	heightPercentage = .5


	def __init__(self, displaySize):
		self.active = False
		self.updateStack = False
		self.pipeForText = []


		self.cursorField = 5, 10
		self.cursorFieldSurface = pygame.Surface(self.cursorField)
	
		self.prompt = '>>>'


		self.textBoxSize = displaySize[0] * Console.widthPercentage, displaySize[1] * Console.heightPercentage 
		self.textBox = pygame.Surface(self.textBoxSize)
		self.textBox = self.textBox.convert_alpha()
		self.TEAL = pygame.Color(0, 128, 128, 50)
		self.textBox.fill(self.TEAL)

	def updateTextBox(self, newScreenSize):
		self.textBoxSize = newScreenSize[0] * Console.widthPercentage, newScreenSize[1] * Console.heightPercentage
		self.textBox = pygame.Surface(self.textBoxSize)
		self.textBox.fill(TEAL)
		
		
	def update(self,):
		if self.active:
			if self.updateStack:
				Game.drawStack.append(self.textBox) #make an object to handle this.
		elif not self.active:
			if not self.updateStack:
				if Game.drawStack:
					Game.drawStack.pop()

	def textField(self, ):
		pass
		
	def textSystem(self, pos):
		textField()
		for char in self.buffer:
			pass	
		
		
		
					
	def activate(self, ):
		print 'its updating.'
		if self.active:
			self.active = False
			self.updateStack = False
		elif not self.active:
			self.active = True
			self.updateStack = True


class Game(object):
	"""This is the game object that starts the game pulls in display and starts working on it. This is like the 'Heart' organ of the program."""
	drawStack = []
	def __init__(self, ):
		self.displayForGame = pygame.display.get_surface()
		self.displayForGameRect = self.displayForGame.get_rect()
		self.displayForGameSize = self.displayForGame.get_size()
	def Run(self, ):
		self.GameLoop()

	def GameLoop(self):
		print self.displayForGame
		gameRunning = True
		while gameRunning:
			clock.tick(FPS)
			pygame.display.set_caption('{} fps | {} active | {} updateStack | {} drawStack'.format(int(clock.get_fps()),console.active, console.updateStack, len(self.drawStack)))	
			for event in pygame.event.get():
				if event.type == KEYUP:
					if event.key == K_q or event.key == K_ESCAPE:
						gameRunning = False
					elif event.key == Console.summon:
						console.activate()
				if event.type == pygame.VIDEORESIZE:
					self.displayForGame = pygame.display.get_surface()
					self.displayForGameRect = self.displayForGame.get_rect()
					self.displayForGameSize = self.displayForGame.get_size()
					self.displayForGameSize = pygame.display.get_surface().get_size()

					console.updateTextBox(self.displayForGameSize)

			self.update()
			#print Game.drawStack,
		self.quit()

	def quit(self, ):
		pygame.quit()

	def clearScreen(self,):
		self.displayForGame.fill(WHITE)
	def update(self, ):
		self.clearScreen()
		console.update()
		for item in Game.drawStack:
			self.displayForGame.blit(item, (0, 0))
		pygame.display.flip()
		
					
game = Game()	
console = Console(game.displayForGameSize)

