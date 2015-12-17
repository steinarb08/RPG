import Ability
import CombatTeam
import Creature
import AbilityEffect
import random
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

		if targetType == 1 or targetType == 3: #Enemy
			self._GetEnemyTargets()

		if targetType == 2 or targetType == 4: #Friend
			self._GetFriendTargets()

		if targetType == 5: #Any
			self._GetFriendTargets()
			self._GetEnemyTargets()

		if targetType == 6: #All
			for i in range(self._friendTeam.GetTeamSize()):
				if self._friendTeam.GetTeamMember(i).IsAlive():
					self.AddTarget(self._friendTeam.GetTeamMember(i))

			for j in range(self._enemyTeam.GetTeamSize()):
				if self._enemyTeam.GetTeamMember(j).IsAlive():
					self.AddTarget(self._enemyTeam.GetTeamMember(j))

		if targetType == 7: #All Enemies
			for i in range(self._enemyTeam.GetTeamSize()):
				if self._enemyTeam.GetTeamMember(i).IsAlive():
					self.AddTarget(self._enemyTeam.GetTeamMember(i))

		if targetType == 8: #All Friends
			for i in range(self._friendTeam.GetTeamSize()):
				if self._friendTeam.GetTeamMember(i).IsAlive():
					self.AddTarget(self._friendTeam.GetTeamMember(i))

		if targetType == 9: #Random
			self._GetFriendTargets()
			self._GetEnemyTargets()
			for i in range(self._ability.GetTargetNumber()):
				print len(self._possibleTargets)
				self.AddTarget(self._possibleTargets[random.randint(0,len(self._possibleTargets) - 1)])

		if targetType == 10: #Random Enemy
			self._GetEnemyTargets()
			for i in range(self._ability.GetTargetNumber()):
				self.AddTarget(self._possibleTargets[random.randint(0,len(self._possibleTargets) - 1)])

		if targetType == 11: #Random Friend
			self._GetFriendTargets()
			for i in range(self._ability.GetTargetNumber()):
				self.AddTarget(self._possibleTargets[random.randint(0,len(self._possibleTargets) - 1)])


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
