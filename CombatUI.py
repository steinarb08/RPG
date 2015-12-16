import CombatTeam
import Creature
import Combat
import sys
import AbilityTargeting
class CombatUI:


	def __init__(self,playerTeam,enemyTeam):
		self._combat = Combat.Combat(playerTeam,enemyTeam)

	def MainScreen(self):
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
		elif choice == '2':
			print 'Ability'
		elif choice == '3':
			self.PrintAllies()
		elif choice == '4':
			self.PrintEnemies()
		else:
			print 'Invalid input!'
			self.MainScreen()


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
		targetSys = AbilityTargeting.AbilityTargeting(self._combat.GetPlayerTeam(),self._combat.GetEnemyTeam(),ability)
		posTargets = targetSys.GetPossibleTargets()
		print '----------------------------'
		for i in range(len(posTargets)):
			name = posTargets[i].GetName()
			curh = posTargets[i].GetCurrentHealth()
			maxh = posTargets[i].GetMaximumHealth()
			print("{}) {} - {}/{} Health".format(i,name,curh,maxh))
		target = int(raw_input("Choose a target: "))
		# To be continued...