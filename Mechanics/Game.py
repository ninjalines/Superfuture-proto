#/usr/bin/env python
"""Game.py"""
import Constants
from Constants import *
from Extras import *
import pygame
from pygame.locals import *



class Game(object):
	"""This is the game object that starts the game pulls in display and starts working on it. This is like the 'Heart' organ of the program."""
	def __init__(self, ):
		self.display = Display()
		self.console = Console()
		self.drawStack = DrawStack()
		self.chamber = self.Setup()
		self.drawStack.addChamber(self.chamber)
	def Setup(self, ):
		chamber = Chamber((self.display, self.console, BlackBox((50, 50), (0, 0))))
		return chamber	 
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
					elif event.key == K_UP or event.key = K_w:
						pass
					elif event.key == K_DOWN or event.key = K_s:
						pass
					elif event.key == K_RIGHT or event.key = K_d:
						pass
					elif event.key == K_LEFT  or event.key = K_a:
						pass
				if event.type == pygame.VIDEORESIZE:
					self.display.updateScreen()

					console.updateTextBox(self.display.displaySize)

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
		
		pygame.display.flip()
		
					
class Console(object):
	CONSOLE = CONSOLE
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
		self.image = self.textBox
		self.posisition = 0, 0

	def updateTextBox(self, newScreenSize):
		self.textBoxSize = newScreenSize[0] * Console.widthPercentage, newScreenSize[1] * Console.heightPercentage
		self.textBox = pygame.Surface(self.textBoxSize)
		self.textBox.fill(TEAL)
		self.image = self.textBox
		
		
	def update(self,):
		print Game.drawStack,
		if not self.isOnDrawStack():
			Game.drawStack.append(self.textBox)
		elif self.isOnDrawStack():
			pass

			
	def isOnDrawStack(self, ):
		if Game.drawStack:
			return True
		else:
			return False	

	def textField(self, ):
		pass
		
	def textSystem(self, pos):
		textField()
		for char in self.buffer:
			pass	

pygame = Pygame()
game = Game()	


