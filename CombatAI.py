import CombatTeam
import AbilityExecute
class CombatAI:

	def __init__(self, playerTeam,computerTeam,creature):
		self._playerTeam = playerTeam
		self._computerTeam = computerTeam
		self._curCreature = creature
		self._ability = 0 # Chosen ability
		self._target = 0 #C Chosen target

	def AI(self):
		self.ChooseAbility()
		self.ChooseTarget()

	def ChooseAbility(self): #chooses basic attack
		self._ability = creature.GetAbility(0)


	def ChooseTarget(self): #Chooses creature with lowest health
		self._target = self.FindLowestHealthEnemy()


	def FindLowestHealthEnemy(self):
		creature = 0
		healthCompare = playerTeam.GetHighestHealth()
		for i in range(playerTeam.GetTeamSize()):
			if playerTeam.GetTeamMember(i).GetCurrentHealth() <= healthCompare:
				creature = playerTeam.GetTeamMember(i)
				healthCompare = creature.GetCurrentHealth()
		return creature


	def GetTarget(self):
		return self._target

	def GetAbility(self):
		return self._ability

	def ExecuteAbility(self):
		exe = AbilityExecute.AbilityExecute(self._ability,self._curCreature,self._target)
		exe.UseAbility()