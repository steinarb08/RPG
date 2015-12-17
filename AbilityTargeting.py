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


	def GetPossibleTargets(self):
		targetType = self._ability.GetTargetType()

		if targetType == 1: # Enemy
			self._GetSingleEnemyTargets()

		return self._possibleTargets

	def AddTarget(self,creature):
		self._chosenTargets.append(creature)


	def GetAllChosenTargets(self):
		return self._chosenTargets

	def GetChosenTarget(self,n):
		return self._chosenTargets[n]

	def _GetSingleEnemyTargets(self):
		for i in range(self._enemyTeam.GetTeamSize()):
			if self._enemyTeam.GetTeamMember(i).IsAlive():
				self._possibleTargets.append(self._enemyTeam.GetTeamMember(i))
