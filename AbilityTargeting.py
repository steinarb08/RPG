import Ability
import CombatTeam
import Creature
import AbilityEffect
class AbilityTargeting:

	def __init__(self,friendTeam,enemyTeam,ability,curCreature):
		self._friendTeam = friendTeam
		self._enemyTeam = enemyTeam
		self._ability = ability
		self._chosenTargets = []
		self._possibleTargets = []
		self._curCreature = curCreature


	def GetPossibleTargets(self):
		targetType = self._ability.GetTargetType()

		if targetType == 1 or 3: # Enemy
			self._GetEnemyTargets()

		if targetType == 2 or 4: # Friend
                        self._GetFriendTargets()

                if targetType == 5: # Any
                        slef._GetAnyTargets()

		return self._possibleTargets

	def AddTarget(self,creature):
		self._chosenTargets.append(creature)


	def GetAllChosenTargets(self):
		return self._chosenTargets

	def GetChosenTarget(self,n):
		return self._chosenTargets[n]

	def _GetEnemyTargets(self):
		for i in range(self._enemyTeam.GetTeamSize()):
			if self._enemyTeam.GetTeamMember(i).IsAlive():
				self._possibleTargets.append(self._enemyTeam.GetTeamMember(i))

	def _GetFriendTargets(self):
                for i in range(self._friendTeam.GetTeamSize()):
                        if self._friendTeam.GetTeamMember(i).IsAlive():
                                self._possibleTargets.append(self._friendTeam.GetTeamMember(i))

        def _GetAnyTargets(self):
                for i in range(self._friendTeam.GetTeamSize()):
                        if self._friendTeam.GetTeamMember(i).IsAlive():
                                self._possibleTargets.append(self._friendTeam.GetTeamMember(i))
                for j in range(self._enemyTeam.GetTeamSize()):
			if self._enemyTeam.GetTeamMember(j).IsAlive():
				self._possibleTargets.append(self._enemyTeam.GetTeamMember(j))
