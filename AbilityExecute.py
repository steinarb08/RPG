import Ability
import AbilityEffect
import Creature
class AbilityExecute:

	def __init__(self,ability,caster,target):
		self._ability = ability
		self._caster = caster
		self._target = target
		self._scaleAttribute = 0 # Ammount of attribute caster has
		self._scalerType = 0 # Type of scaler that is used (strength,spellpower...)

	# Only function called outside class
	def UseAbility(self):
		Effects = self._ability.GetEffects()

		for i in range(len(Effects)):
			self._GetScalerValue(i)
			self._scalerType = Effects[i].GetScalerType()
			if Effects[i].GetEffectType() == 0: #physical damage
				self._ApplyPhysicalDamage(Effects[i])
			elif Effects[i].GetEffectType() == 1: #Heal
				self._ApplyHeal(Effects[i])
			elif Effects[i].GetEffectType() == 2: #Fire Damage
				self._ApplyFireDamage(Effects[i])
			elif Effects[i].GetEffectType() == 3: #Water Damage
				self._ApplyWaterDamage(Effects[i])
			elif Effects[i].GetEffectType() == 4: #Air Damage
				self._ApplyAirDamage(Effects[i])
			elif Effects[i].GetEffectType() == 5: #Darkness Damage
				self._ApplyDarknessDamage(Effects[i])
			elif Effects[i].GetEffectType() == 6: #Light Damage
				self._ApplyLightDamage(Effects[i])
			elif Effects[i].GetEffectType() == 7: #Stunned
				self._target.AddEffect(Effects[i],self._caster)
			elif Effects[i].GetEffectType() == 8: #Physical DoT
				self._target.AddEffect(Effects[i],self._caster)
			elif Effects[i].GetEffectType() == 9: #HoT
				self._target.AddEffect(Effects[i],self._caster)
			elif Effects[i].GetEffectType() == 10: #Fire DoT
				self._target.AddEffect(Effects[i],self._caster)
			elif Effects[i].GetEffectType() == 11: #Water DoT
				self._target.AddEffect(Effects[i],self._caster)
			elif Effects[i].GetEffectType() == 12: #Air DoT
				self._target.AddEffect(Effects[i],self._caster)
			elif Effects[i].GetEffectType() == 13: #Darkness DoT
				self._target.AddEffect(Effects[i],self._caster)
			elif Effects[i].GetEffectType() == 14: #Light DoT
				self._target.AddEffect(Effects[i],self._caster)


	def UsePeriodicAbility(self):
		Effects = self._ability.GetEffects()
		for i in range(len(Effects)):
			print i
			print Effects[i].GetEffectType()
			self._GetScalerValue(i)
			self._scalerType = Effects[i].GetScalerType()
			if Effects[i].GetEffectType() == 8: #Physical DoT
				self._ApplyPhysicalDamage(Effects[i])
			elif Effects[i].GetEffectType() == 9: #HoT
				self._ApplyHeal(Effects[i])
			elif Effects[i].GetEffectType() == 10: #Fire DoT
				self._ApplyFireDamage(Effects[i])
			elif Effects[i].GetEffectType() == 11: #Water DoT
				self._ApplyWaterDamage(Effects[i])
			elif Effects[i].GetEffectType() == 12: #Air DoT
				self._ApplyAirDamage(Effects[i])
			elif Effects[i].GetEffectType() == 13: #Darkness DoT
				self._ApplyDarknessDamage(Effects[i])
			elif Effects[i].GetEffectType() == 14: #Light DoT
				self._ApplyLightDamage(Effects[i])


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
	def _ApplyFireDamage(self,effect):
		damage = effect.GetTotalValue(self._scaleAttribute)
		self._target.AddCurrentHealth(-damage)
	def _ApplyWaterDamage(self,effect):
		damage = effect.GetTotalValue(self._scaleAttribute)
		self._target.AddCurrentHealth(-damage)
	def _ApplyAirDamage(self,effect):
		damage = effect.GetTotalValue(self._scaleAttribute)
		self._target.AddCurrentHealth(-damage)
	def _ApplyDarknessDamage(self,effect):
		damage = effect.GetTotalValue(self._scaleAttribute)
		self._target.AddCurrentHealth(-damage)
	def _ApplyLightDamage(self,effect):
		damage = effect.GetTotalValue(self._scaleAttribute)
		self._target.AddCurrentHealth(-damage)
