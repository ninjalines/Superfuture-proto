#!/usr/bin/env python

from Constants import *
import pygame

class Length(object):
	def __init__(self, up, down, left, right, speed):
		self.up = up
		self.down = down
		self.left = left
		self.right = right
		self.speed = speed

	def setLength(self, up, down, left, right, speed):
		self.up = up
		self.down = down
		self.left = left
		self.right = right
		

	def setSpeed(self, speed):
		self.speed = speed

	def setModification(self, modificationObject):
		#self.modify(modificationObject, iD)
		pass

	def modify(self, modifyObject, iD):
		#if modifyObject.op == 0:
			#self.up = modifyObject.modifyingValueUp + self.up
			#self.down = modifyObjectmodifyingValueDown + self.down
			#self.
		pass

class Movement(Length):
	def __init__(self, up, down, left, right, speed ):
		super(Movement, self).__init__(self, up, down, left, right, speed)
		self.DIRECTIONAL = {UP:0, DOWN:0, LEFT:0, RIGHT:0, UPRIGHT:[0, 0], UPLEFT:[0, 0], DOWNRIGHT:[0, 0], DOWNLEFT:[0, 0]}
		self.DIRECTIONAL[UP] = up
		self.DIRECTIONAL[DOWN] = down
		self.DIRECTIONAL[LEFT] = left
		self.DIRECTIONAL[RIGHT] = right
		self.DIRECTIONAL[UPRIGHT][0] = self.DIRECTIONAL[UP]
		self.DIRECTIONAL[UPRIGHT][1] = self.DIRECTIONAL[RIGHT]
		self.DIRECTIONAL[UPLEFT][0] = self.DIRECTIONAL[UP]
		self.DIRECTIONAL[UPLEFT][1] = self.DIRECTIONAL[LEFT]
		self.DIRECTIONAL[DOWNRIGHT][0] = self.DIRECTIONAL[DOWN]
		self.DIRECTIONAL[DOWNRIGHT][1] = self.DIRECTIONAL[RIGHT]
		self.DIRECTIONAL[DOWNLEFT][0] = self.DIRECTIONAL[DOWN]
		self.DIRECTIONAL[DOWNLEFT][1] = self.DIRECTIONAL[LEFT]

 

class Unit(object):
	"""The base unit for objects that move, stand still and have functionality for these 'units'."""
	identificationNumber = 0
	def __init__(self, size, position ):
		self.identification = PLAYER
		self.identificationNumber = Unit.identificationNumber
		Unit.identificationNumber += 1
		self.size = size
		self.position = position
		self.image = pygame.Surface(self.size)
		self.rect = self.image.get_rect()
	
	def returnIdentificationNumber(self, ):
		identificationNumber = Unit.identificationNumber
		Unit.identificationNumber += 1
		return identificationNumber
	def returnIdentification(self, ):
		identification = Unit.identification
		return identification
	def ai(self, ):
		pass

		
	def movement(self, direction):
		pass
			
			

			

class BlackBox(Unit):
	def __init__(self, size, position):
		super(BlackBox, self).__init__(size, position)
		self.image.fill(BLACK)
		self.position = position
		self.identification = self.returnIdentification()
	def returnIdentification(self, ):
		identification = PLAYER
		return identification



			

class Management(object):
	ManagementGroup = []
	identificationNumber = 0
	identification = MANAGEMENT
	def __init__(self, ):
		Management.ManagementGroup.append(self)

	def returnIdentification(self, ):
		identification = Management.ManagementIdentification
		Management.ManagementIdentification += 1
		return identification

	def doesManagementExist(self, ):
		pass					

class UnitManagement(Management):
	UnitManagementGroup = []
	UnitManagementIdentification = 0
	def __init__(self, ):
		super(UnitManagement, self).__init__(self, )
		UnitManagement.UnitManagementGroup.append(self)
		self.identification = self.returnIdentification()

	def returnIdentification(self, ):
		ident = UnitManagement.UnitManagementIdentification
		UnitManagement.UnitManagementIdentification += 1
		return ident


	
