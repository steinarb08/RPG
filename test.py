import Creature
import CombatTeam
import Combat
import Ability
import CombatUI
import AbilityEffect
c1 = Creature.Creature("Steinar")
c2 = Creature.Creature("Benni")
c1.AddAttributes(1)
playerTeam = CombatTeam.CombatTeam()
playerTeam.AddToTeam(c1)

enemyTeam = CombatTeam.CombatTeam()
enemyTeam.AddToTeam(c2)


userInt = CombatUI.CombatUI(playerTeam,enemyTeam)

k =0
while k==0:
	userInt.MainScreen()



