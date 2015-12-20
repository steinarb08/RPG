import AbilityEffect
class Ability:

	TargetType = ('Self','Enemy','Friend','Enemies','Friends','Any','All','AllEnemies',
		'AllFriends','Random','RandomEnemy','RandomFriend')

	def __init__(self,name,targettype,targetnum):
		self._name = name
		self._targetType = targettype
		self._targetNumber = targetnum
		self._effects = []


	def GetName(self):
		return self._name

	def AddEffect(self,effect):
		self._effects.append(effect)

	def GetEffect(self,n):
		return self._effects[n]

	def GetEffects(self):
		return self._effects

	def GetTargetNumber(self):
		return self._targetNumber

	def SetName(self,name):
		self._name = name

	def SetTargetNumber(self,number):
		self._targetNumber = number

	def GetTargetType(self):
		return self._targetType

	def RemoveEffect(self,n):
		self._effects.pop(n)