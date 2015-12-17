import CombatTeam
import Creature
class Combat:

	def __init__(self,playerTeam,enemyTeam):
		self._playerTeam = playerTeam
		self._orgPlayerTeam = playerTeam
		self._enemyTeam = enemyTeam
		self._orgEnemyTeam = enemyTeam
		self._round = 1
		self._victory = 0
		self._defeat = 0
		self._curCreature = 0
		self._curTeam = 0
		self._oppTeam = 0
		self._isPlayerTeam = 0
		self._slowestCreature = 0
		

		for i in range(playerTeam.GetTeamSize()):
			self._playerTeam.GetTeamMember(i).SetCurrentHealthMax()
			self._playerTeam.GetTeamMember(i).SetCurrentInitiativeMax()

		for i in range(enemyTeam.GetTeamSize()):
			self._enemyTeam.GetTeamMember(i).SetCurrentHealthMax()
			self._enemyTeam.GetTeamMember(i).SetCurrentInitiativeMax()

		self.FindCurrentCreature()
		self.FindSlowestCreature()


	def FindCurrentCreature(self):
		lowestInit = 0
		curCreature = 0
		curTeam = 0
		oppTeam = 0
		for i in range(self._playerTeam.GetTeamSize()):
			if(self._playerTeam.GetTeamMember(i).GetCurrentInitiative() > lowestInit and self._playerTeam.GetTeamMember(i).GetCurrentHealth() > 0):
				lowestInit = self._playerTeam.GetTeamMember(i).GetCurrentInitiative()
				curCreature = self._playerTeam.GetTeamMember(i)
				curTeam = self._playerTeam
				oppTeam = self._enemyTeam
				self._isPlayerTeam = True
		for i in range(self._enemyTeam.GetTeamSize()):
			if(self._enemyTeam.GetTeamMember(i).GetCurrentInitiative() > lowestInit and self._enemyTeam.GetTeamMember(i).GetCurrentHealth() > 0):
				curTeam = self._enemyTeam
				oppTeam = self._playerTeam
				curCreature = curTeam.GetTeamMember(i)
				lowestInit = curCreature.GetCurrentInitiative()
				self._isPlayerTeam = False
		self._curCreature = curCreature
		self._curTeam = curTeam
		self._oppTeam = oppTeam


	def FindSlowestCreature(self):
		init = 150000
		slowCreature = 0
		for i in range(self._playerTeam.GetTeamSize()):
			if(self._playerTeam.GetTeamMember(i).GetMaximumInitiative()<init):
				init = self._playerTeam.GetTeamMember(i).GetMaximumInitiative()
				slowCreature = self._playerTeam.GetTeamMember(i)
		for i in range(self._enemyTeam.GetTeamSize()):
			if(self._enemyTeam.GetTeamMember(i).GetMaximumInitiative()<init):
				init = self._enemyTeam.GetTeamMember(i).GetMaximumInitiative()
				slowCreature = self._enemyTeam.GetTeamMember(i)
		self._slowestCreature = slowCreature

	# Checks if victory/defeat conditions are met and sets the appropriate parameters
	def CheckForVictory(self):
		if len(self._playerTeam.GetAliveMembers()) == 0:
			self._defeat = 1
		if len(self._enemyTeam.GetAliveMembers()) == 0:
			self._victory = 1


	def NextCreature(self):
		self._curCreature.AddCurrentInitiative(-self._slowestCreature.GetMaximumInitiative())
		self.CheckForVictory()
		self.EndRoundCheck()
		self.FindCurrentCreature()

	def NewRound(self):
		self._round+=1

		for i in range(self._playerTeam.GetTeamSize()):
			self._playerTeam.GetTeamMember(i).SetCurrentInitiativeMax()
		for i in range(self._enemyTeam.GetTeamSize()):
			self._enemyTeam.GetTeamMember(i).SetCurrentInitiativeMax()

	def EndRoundCheck(self):
		newRound = True
		for i in range(self._playerTeam.GetTeamSize()):
			if(self._playerTeam.GetTeamMember(i).GetCurrentInitiative() >= self._slowestCreature.GetMaximumInitiative()):
				newRound = False
		for i in range(self._enemyTeam.GetTeamSize()):
			if(self._enemyTeam.GetTeamMember(i).GetCurrentInitiative() >= self._slowestCreature.GetMaximumInitiative()):
				newRound = False
		if newRound:
			self.NewRound()


	def GetCurrentCreature(self):
		return self._curCreature

	def IsPlayerTeam(self):
		return self._isPlayerTeam

	def GetPlayerTeam(self):
		return self._playerTeam

	def GetEnemyTeam(self):
		return self._enemyTeam



