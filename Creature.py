import Attributes
import Ability
class Creature:

	# Constant variables used to calculate various things
	_constHealth = 10
	_constInitiative = 10


	# Constructor, creates a private variable _name from input and creates base attributes
	def __init__(self, name):
		self._name = name
		self._attributes = Attributes.Attributes()
		self._curHealth = self.GetMaximumHealth()
		self._curInitiative = self.GetMaximumInitiative
		self._abilities = []

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