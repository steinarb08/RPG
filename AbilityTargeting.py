import Ability
import CombatTeam
import Creature
import AbilityEffect
class AbilityTargeting:

	def __init__(self,friendTeam,enemyTeam,ability):
		self._friendTeam = friendTeam
		self._enemyTeam = enemyTeam
		self._ability = ability
		self._chosenTargets = []
		self._possibleTargets = []


	# This is the only function called from outside this class!
	def GetPossibleTargets(self):
		targetType = self._ability.GetTargetType()

		if targetType == 1: # Enemy
			self._GetSingleEnemyTargets()

		return self._possibleTargets




	def _GetSingleEnemyTargets(self):
		for i in range(self._enemyTeam.GetTeamSize()):
			if self._enemyTeam.GetTeamMember(i).IsAlive():
				self._possibleTargets.append(self._enemyTeam.GetTeamMember(i))