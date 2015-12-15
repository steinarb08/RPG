import Creature
class CombatTeam:

	def __init__(self):
		self._teamSize = 0
		self._team = []


	def AddToTeam(self, n):
		self._team.append(n)
		self._teamSize += 1

	def GetTeamSize(self):
		return self._teamSize

	def GetTeamMember(self,n):
		return self._team[n]

	def GetHighestHealth(self):
		maxHealth = 0
		for i in range(self._teamSize):
			if(self._team[i].GetCurrentHealth() > maxHealth):
				maxHealth = self._team[i].GetCurrentHealth()
		return maxHealth

	def GetAliveMembers(self):
		aliveList = []
		for i in range(self._teamSize):
			if(self._team[i].GetCurrentHealth > 0):
				aliveList.append(self._team[i])
		return aliveList