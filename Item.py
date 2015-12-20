class Item:

	'''
	Slots:
		0 : weapon 1h
		1 : weapon 2h
		2 : offhand
		3 : armor
		4 : helm
		5 : boots
		6 : gloves
	'''


	def __init__(self,name,slot):
		self._name = name
		self._slot = slot
		self._abilities = []
		self._resistances = []
		self._bonusDamage = []
		self._bonusAttributes = []



	def GetName(self):
		return self._name
	def GetSlot(self):
		return self._slot
	def GetAbilities(self):
		return self._abilities
	def GetResistances(self):
		return self._resistances
	def GetBonusDamage(self):
		return self._bonusDamage
	def GetBonusAttributes(self):
		return self._bonusAttributes

	def SetName(self,name):
		self._name = name
	def SetSlot(self,slot):
		self._slot = slot
	def SetAbilities(self,abilities):
		self._abilities = abilities
	def SetResistances(self,resistances):
		self._resistances = resistances
	def SetBonusDamage(self, bonusDamage):
		self._bonusDamage = bonusDamage
	def SetBonusAttributes(self,attributes):
		self._bonusAttributes = attributes

	def AddAbility(self,ability):
		self._abilities.append(ability)