import CombatTeam
import Creature
import Combat
import sys
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
			print 'Attack'
		elif choice == '2':
			print 'Ability'
		elif choice == '3':
			print 'See allies'
		elif choice == '4':
			print 'See enemies'
		else:
			print 'Invalid input!'
			self.MainScreen()

