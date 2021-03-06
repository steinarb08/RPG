import Attributes
import Ability
import LoadResources
import pygame
import os
from pygame.locals import *
class Creature(pygame.sprite.Sprite):

	# Constant variables used to calculate various things
	_constHealth = 10
	_constInitiative = 10
	_equipmentSlots = 7

	# Constructor, creates a private variable _name from input and creates base attributes
	def __init__(self, name):
		pygame.sprite.Sprite.__init__(self)
		self._name = name
		self._attributes = Attributes.Attributes()
		self._curHealth = self.GetMaximumHealth()
		self._curInitiative = self.GetMaximumInitiative
		self._abilities = []
		self._effects = []
		self._effDuration = []
		self._effCaster = []
		self._itemsInventory = []
		self._itemsEquipped = []
		self.SetImage()

		for i in range(self._equipmentSlots):
			self._itemsEquipped.append(None)


	def GetName(self):
		return self._name

	def SetName(self,n):
		self._name = n

	# Sets all attributes to a fixed value n
	def SetAttributes(self,n):
		self._attributes.SetAllAttributes(n)

	# Adds n to all attributes
	def AddAttributes(self,n):
		self._attributes.AddAllAttributes(n)

	# Returns attributes
	def GetAttributes(self):
		return self._attributes

	def GetMaximumHealth(self):
		return self._attributes.GetToughness()*Creature._constHealth

	def GetMaximumInitiative(self):
		return self._attributes.GetQuickness()*Creature._constInitiative

	def GetCurrentHealth(self):
		return self._curHealth

	def GetCurrentInitiative(self):
		return self._curInitiative

	def SetCurrentHealth(self,n):
		self._curHealth = n

	def SetCurrentHealthMax(self):
		self._curHealth = self.GetMaximumHealth()

	def SetCurrentInitiative(self,n):
		self._curInitiative = n

	def SetCurrentInitiativeMax(self):
		self._curInitiative = self.GetMaximumInitiative()

	def AddCurrentHealth(self,n):
		self._curHealth += n

	def AddCurrentInitiative(self,n):
		self._curInitiative += n

	def AddAbility(self,n):
		self._abilities.append(n)

	def GetAbilities(self):
		return self._abilities

	def GetAbility(self,n):
		return self._abilities[n]

	def GetEffects(self):
		return self._effects

	def GetDurations(self):
		return self._effDuration

	def GetCaster(self):
		return self._effCaster

	def SetDuration(self,n,i):
		self._effDuration[n] = i

	def AddEffect(self, eff, cas):
		self._effects.append(eff)
		self._effDuration.append(eff.GetDuration())
		self._effCaster.append(cas)

	def ResetEffects(self):
		self._effects = []
		self._effDuration = []
		self._effCaster = []

	def RemoveEffect(self,n):
		self._effects.pop(n)
		self._effDuration.pop(n)
		self._effCaster.pop(n)

	def IsDead(self):
		if self.GetCurrentHealth <0:
			return True
		else:
			return False

	def IsAlive(self):
		if self.GetCurrentHealth > 0:
			return True
		else:
			return False


	def StashItem(self,item):
		self._itemsInventory.append(item)
	def GetInventory(self):
		return self._itemsInventory
	def GetEquipment(self):
		return self._itemsEquipped
	def EquipItem(self,item):
		slot = item.GetSlot()
		if not self._itemsEquipped[slot]:
			self._itemsEquipped.insert(slot,item)
		else:
			curItem = self._itemsEquipped[slot].pop()
			self._itemsEquipped.insert(slot,item)
			self._itemsInventory.append(curItem)
	def GetItemInSlot(self,slot):
		return self._itemsEquipped[slot]


	def SetImage(self):
		fullname = os.path.join('data', (self._name +'.jpg'))
		self._image = pygame.image.load(fullname)
		self._imagerect = self._image.get_rect()

	def GetImage(self):
		return self._image

	def GetImageRect(self):
		return self._imagerect

	def update(self, pos):
		self._rect.topleft = pos
