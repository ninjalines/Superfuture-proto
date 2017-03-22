#/usr/bin/env python
"""Game.py"""
import Constants
from Constants import *
from Extras import *
from Unit import *
import pygame
from pygame.locals import *



class Game(object):
	"""This is the game object that starts the game pulls in display and starts working on it. This is like the 'Heart' organ of the program."""
	def __init__(self, ):
		self.display = Display()
		self.console = Console(pygame.display.get_surface().get_size())
		self.drawStack = DrawStack()
		self.chamber = self.Setup()
		self.drawStack.addChamber(self.chamber)
	def Setup(self, ):
		return Chamber(None, None, self.display, self.console, BlackBox((50, 50), (0, 0)))	 
	def Run(self, ):
		self.GameLoop()

	def GameLoop(self):
		gameRunning = True
		while gameRunning:
			clock.tick(FPS)
			#pygame.display.set_caption('{} fps | {} active | {} updateStack | {} drawStack'.format(int(clock.get_fps()),console.active, console.updateStack, len(self.drawStack)))	
			for event in pygame.event.get():
				if event.type == KEYUP:
					if event.key == K_q or event.key == K_ESCAPE:
						gameRunning = False
					elif event.key == K_BACKQUOTE:
						self.console.turnOn()
					elif event.key == K_UP or event.key == K_w:
						pass
					elif event.key == K_DOWN or event.key == K_s:
						pass
					elif event.key == K_RIGHT or event.key == K_d:
						pass
					elif event.key == K_LEFT  or event.key == K_a:
						pass
				if event.type == pygame.VIDEORESIZE:
					self.display.updateScreen(self.chamber, event.size)
					self.console.updateTextBox(event.size, self.chamber)

			self.update()
			#print Game.drawStack,
		self.quit()

	def quit(self, ):
		pygame.quit()

	def clearScreen(self,):
		self.display.display.fill(WHITE)
	def update(self, ):
		self.clearScreen()
		self.console.update(self.chamber)
		self.drawStack.update()
		
		pygame.display.flip()
		
					
class Console(object):
	fontColor = RED
	
	widthPercentage = .8
	heightPercentage = .5


	def __init__(self, displaySize):
		self.font = pygame.font.SysFont('ubuntumono', 10, True, False)
		self.active = False
		self.updateStack = False
		self.pipeForText = []
		self.cursorField = 5, 10
		self.cursorFieldSurface = pygame.Surface(self.cursorField)
		self.prompt = '>>>'
		self.on = False
		#important stuff thus far
		#takes 80% of the width and 50% of the height 
		self.textBoxSize = displaySize[0] * Console.widthPercentage, displaySize[1] * Console.heightPercentage 
		#makes a pygame surface
		self.textBox = pygame.Surface(self.textBoxSize)
		#converts to alpha for alpha layer over the color
		self.textBox = self.textBox.convert_alpha()
		self.textBox.fill(TEAL)
		#the image variable for the Chamber and DrawStack
		self.image = self.textBox
		#position for the location of the blit 
		self.position = 0, 0
		#identification for the name in Chamber object
		self.identification = CONSOLE
		self.setup()

	def setup(self, ):
		self.textSize = 5, 11
		self.textSizeWidth = 
		self.promptSize = CharacterBuffer.returnSize(self.prompt)
		self.xmargin = 5
		self.ymargin = 10
		self.margin = self.promptSize + self.xmargin, self.ymargin
		self.startingAbscissa = self.margin[0]
		self.promptAbscissa = self.xmargin

	def updateTextSize(self, size=8 ):
		maxSizeNeededForText = Console.callCharacterBufferResize(size)
	@staticmethod
	def callCharacterBufferResize(size):
		arguments = 
		maxSize = findBiggest(arguments)
		return maxSize
	def updateLineCoordinates(self, ):
		self.charactersPerLinePrompt = ()
		self.charactersPerLine = (self.textBoxSize[0] - self.xmargin) / self.textSize[0]
		self.charactersPerColumn
	def createArray(self, ):
		self.charactersPerLinePrompt = (self.textBoxSize[0]-self.margin[0])/self.textSize[0]	
		self.charactersPerLine = (self.textBoxSize[0] - self.xmargin)/self.textSize[0]
		self.charactersPerColumn = self.textBoxSize[1]/self.textSize[1]
	#need array being returned that has all the coordinates of the characters 
	#in an entire line
	#needs: how many characters fit in a line(in case of resize)
	def nextLine(self, fullLine=False)
		array = []
		self.charactersPerLinePrompt = (self.textBox)

	def updateTextBox(self, newScreenSize, chamber):
		self.textBoxSize = newScreenSize[0] * Console.widthPercentage, newScreenSize[1] * Console.heightPercentage
		self.textBox = pygame.Surface(self.textBoxSize)
		self.textBox.fill(TEAL)
		self.image = self.textBox
		chamber.items[CONSOLE] = self
		self.setup()

	def turnOn(self, ):
		if not self.on:
			self.on = True
		elif self.on:
			self.on = False

	def update(self, chamber):
		if self.on:
			if not chamber.write[CONSOLE]:
				chamber.write[CONSOLE] = True
		elif not self.on:
			if chamber.write[CONSOLE]:
				chamber.write[CONSOLE] = False
		self.textSystem()
	def gravity(self, ):
		pass
	def textField(self, ):
		pass
		
	def textSystem(self, ):
		self.cursorPosition = 

pg = Pygame()
game = Game()	


