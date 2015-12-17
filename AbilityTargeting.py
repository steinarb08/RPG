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


		if targetType == 0: #Self
			self.AddTarget(self._curCreature)

		if targetType == 1 or 3: #Enemy
			self._GetEnemyTargets()

		if targetType == 2 or 4: #Friend
			self._GetFriendTargets()

		if targetType == 5: #Any
			self._GetFriendTargets()
			self._GetEnemyTargets()

		if targetType == 7: #All Enemies
			for i in range(self._enemyTeam.GetTeamSize()):
				if self._enemyTeam.GetTeamMember(i).IsAlive():
					self.AddTarget(self._enemyTeam.GetTeamMember(i))

		if targetType == 8: #All Friends
			for i in range(self._friendTeam.GetTeamSize()):
				if self._friendTeam.GetTeamMember(i).IsAlive():
					self.AddTarget(self._friendTeam.GetTeamMember(i))


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
