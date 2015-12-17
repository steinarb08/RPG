import Ability
import AbilityEffect
import Creature
class AbilityExecute:

	def __init__(self,ability,caster,target):
		self._ability = ability
		self._caster = caster
		self._target = target
		self._scaleAttribute = 0
		self._scalerType = 0

	# Only function called outside class
	def UseAbility(self):
		Effects = self._ability.GetEffects()

		for i in range(len(Effects)):
			self._GetScalerValue(i)
			if Effects[i].GetEffectType() == 0: #physical damage
				self._scalerType = Effects[i].GetScalerType()
				self._ApplyPhysicalDamage(Effects[i])
			elif Effects[i].GetEffectType() == 1: #Heal
				self._ApplyHeal(Effects[i])


	def _GetScalerValue(self,i):
		if self._scalerType == 0:
			self._scaleAttribute = self._caster.GetAttributes().GetStrength()
		elif self._scalerType == 1:
			self._scaleAttribute = self._caster.GetAttributes().GetStamina()
		elif self._scalerType == 2:
			self._scaleAttribute = self._caster.GetAttributes().GetSpellpower()
		elif self._scalerType == 3:
			self._scaleAttribute = self._caster.GetAttributes().GetConcentration()
		elif self._scalerType == 4:
			self._scaleAttribute = self._caster.GetAttributes().GetToughness()
		elif self._scalerType == 5:
			self._scaleAttribute = self._caster.GetAttributes().GetQuickness()


	def _ApplyPhysicalDamage(self,effect):
		damage = effect.GetTotalValue(self._scaleAttribute)
		self._target.AddCurrentHealth(-damage)
	def _ApplyHeal(self,effect):
		heal = effect.GetTotalValue(self._scaleAttribute)
		self._target.AddCurrentHealth(heal)