class AbilityEffect:

	EffectType = ('PhysicalDamage','Heal')
	ScalerType = ('Strength','Stamina','Spellpower','Concentration','Toughness','Quickness')


	def __init__(self,name,efftype,scalerType,basevalue,scalerValue):
		self._name = name
		self._type = efftype
		self._scalerType = scalerType
		self._baseValue = basevalue
		self._scalerValue = scalerValue


	def GetTotalValue(self,attributenum):
		return self._baseValue + scalerValue*attributenum