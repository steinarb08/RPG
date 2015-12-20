import CombatTeam
import Creature
import Combat
import sys
import AbilityTargeting
import AbilityExecute
import CombatAI
class CombatUI:


	def __init__(self,playerTeam,enemyTeam):
		self._combat = Combat.Combat(playerTeam,enemyTeam)
		self._targetSys = 0

	def MainScreen(self):
		if(self._combat.IsPlayerTeam()):
			print("{}'s turn!".format(self._combat.GetCurrentCreature().GetName()))
			print '----------------------------'
			print '1) Attack'
			print '2) Use ability'
			print '3) See ally status'
			print '4) See enemy status'
			print '0) Quit'
		
			choice = raw_input('Choose an action: ')
			if choice == '0':
				sys.exit()
			elif choice == '1':
				self.ChooseTarget(self._combat.GetCurrentCreature().GetAbility(0))
				self.ExecuteAbility(self._combat.GetCurrentCreature().GetAbility(0))
				self._combat.NextCreature()
			elif choice == '2':
				curAbility = self.ChooseAbility()
				self.ChooseTarget(self._combat.GetCurrentCreature().GetAbility(curAbility))
				self.ExecuteAbility(self._combat.GetCurrentCreature().GetAbility(curAbility))
				self._combat.NextCreature()
			elif choice == '3':
				self.PrintAllies()
			elif choice == '4':
				self.PrintEnemies()
			else:
				print 'Invalid input!'
				self.MainScreen()
		else:
			print self._combat.GetCurrentCreature().GetName()
			ai = CombatAI.CombatAI(self._combat.GetPlayerTeam(),self._combat.GetEnemyTeam(),self._combat.GetCurrentCreature())
			ai.AI()
			self._combat.NextCreature()


	def PrintAllies(self):
		print '----------------------------'
		for i in range(self._combat.GetPlayerTeam().GetTeamSize()):
			name = self._combat.GetPlayerTeam().GetTeamMember(i).GetName()
			curh = self._combat.GetPlayerTeam().GetTeamMember(i).GetCurrentHealth()
			maxh = self._combat.GetPlayerTeam().GetTeamMember(i).GetMaximumHealth()
			print("{}) {} has {}/{} Health".format(i,name,curh,maxh))

	def PrintEnemies(self):
		print '----------------------------'
		for i in range(self._combat.GetEnemyTeam().GetTeamSize()):
			name = self._combat.GetEnemyTeam().GetTeamMember(i).GetName()
			curh = self._combat.GetEnemyTeam().GetTeamMember(i).GetCurrentHealth()
			maxh = self._combat.GetEnemyTeam().GetTeamMember(i).GetMaximumHealth()
			print("{}) {} has {}/{} Health".format(i,name,curh,maxh))


	def ChooseTarget(self,ability):
		self._targetSys = AbilityTargeting.AbilityTargeting(self._combat.GetPlayerTeam(),self._combat.GetEnemyTeam(),ability,self._combat.GetCurrentCreature())
		posTargets = self._targetSys.GetPossibleTargets()
		if ability.GetTargetType() > 0 and ability.GetTargetType() < 6:
			for i in range(ability.GetTargetNumber()):
				print '----------------------------'
				for i in range(len(posTargets)):
					name = posTargets[i].GetName()
					curh = posTargets[i].GetCurrentHealth()
					maxh = posTargets[i].GetMaximumHealth()
					print("{}) {} - {}/{} Health".format(i,name,curh,maxh))
				target = int(raw_input("Choose a target: "))
				self._targetSys.AddTarget(posTargets[target])


	def ExecuteAbility(self,ability):
		for i in range(len(self._targetSys.GetAllChosenTargets())):
			executeProcess = AbilityExecute.AbilityExecute(ability,self._combat.GetCurrentCreature(),self._targetSys.GetChosenTarget(i))
			executeProcess.UseAbility()


	def ChooseAbility(self):
		print '----------------------------'
		for i in range(len(self._combat.GetCurrentCreature().GetAbilities())):
			print("{}) {}".format(i,self._combat.GetCurrentCreature().GetAbility(i).GetName()))
		choice = int(raw_input('Choose an ability: '))
		return choice