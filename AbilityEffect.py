class AbilityEffect:

	EffectType = ('PhysicalDamage','Heal','FireDamage','WaterDamage','AirDamage','DarknessDamage','LightDamage')
	ScalerType = ('Strength','Stamina','Spellpower','Concentration','Toughness','Quickness')


	def __init__(self,name,efftype,scalerType,basevalue,scalerValue):
		self._name = name
		self._type = efftype
		self._scalerType = scalerType
		self._baseValue = basevalue
		self._scalerValue = scalerValue


	def GetTotalValue(self,attributenum):
		return self._baseValue + self._scalerValue*attributenum

	def GetEffectType(self):
		return self._type

	def GetScalerType(self):
		return self._scalerType