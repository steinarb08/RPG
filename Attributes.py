class Attributes:
	# 6 attributes.
	# Strength - increases physical damage, physical ability potency
	# Stamina - increases "mana" for physical abilities and regen for that "mana"
	# Spellpower - increases potency for magical attacks and abilities
	# Concentration - decreases spell fail chance and makes it drop slower
	# Toughness - increases health and resists
	# Quickness - increases speed and initiative


	# _defConstVal adjusts the constructors default value for attributes
	_defConstVal = 10;

	


	# Constructor, creates private instance variables for attributes
	def __init__(self, strength = _defConstVal,stamina = _defConstVal,spellpower = _defConstVal,concentration = _defConstVal,toughness = _defConstVal, quickness = _defConstVal):
 		self._strength = strength
 		self._stamina = stamina
 		self._spellpower = spellpower
 		self._concentration = concentration
 		self._toughness = toughness
 		self._quickness = quickness
 		return


	# Get,set,add for each attributes


	# Strength functions
	def GetStrength(self):
		return self._strength
	def SetStrength(self,strength):
		self._strength = strength
		return
	def AddStrength(self,strength):
		self._strength += strength
		return

	# Stamina functions
	def GetStamina(self):
		return self._stamina
	def SetStamina(self,stamina):
		self._stamina = stamina
		return
	def AddStamina(self,stamina):
		self._stamina += stamina
		return

	# Spellpower functions
	def GetSpellpower(self):
		return self._spellpower
	def SetSpellpower(self,spellpower):
		self._spellpower = spellpower
		return
	def AddSpellpower(self,spellpower):
		self._spellpower += spellpower
		return


	# Concentration functions
	def GetConcentration(self):
		return self._concentration
	def SetConcentration(self,concentration):
		self._concentration = concentration
		return
	def AddConcentration(self,concentration):
		self._concentration += concentration
		return


	# Toughness functions
	def GetToughness(self):
		return self._toughness
	def SetToughness(self,toughness):
		self._toughness = toughness
		return
	def AddToughness(self,toughness):
		self._toughness += toughness
		return


	# Quickness functions
	def GetQuickness(self):
		return self._quickness
	def SetQuickness(self,quickness):
		self._quickness = quickness
		return
	def AddQuickness(self,quickness):
		self._quickness += quickness
		return


	# All stats functions
	def GetAllAttributes(self):
		return self._strength,self._stamina,self._spellpower,self._concentration,self._toughness,self._quickness
	def SetAllAttributes(self,value):
		self._strength = value
		self._stamina = value
		self._spellpower = value
		self._concentration = value
		self._toughness = value
		self._quickness = value
		return
	def AddAllAttributes(self,value):
		self._strength += value
		self._stamina += value
		self._spellpower += value
		self._concentration += value
		self._toughness += value
		self._quickness += value
		return