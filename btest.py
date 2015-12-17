import AbilityTargeting
import Creature
import CombatTeam
import Combat
import Ability
import CombatUI
import AbilityEffect
attack = Ability.Ability('Attack',0,1)
effAttack = AbilityEffect.AbilityEffect('basicAttack',0,0,1,1)
attack.AddEffect(effAttack)
c1 = Creature.Creature("Steinar")
c1.AddAbility(attack)
c2 = Creature.Creature("Benni")
c2.AddAbility(attack)
c1.AddAttributes(1)
playerTeam = CombatTeam.CombatTeam()
playerTeam.AddToTeam(c1)

enemyTeam = CombatTeam.CombatTeam()
enemyTeam.AddToTeam(c2)


userInt = CombatUI.CombatUI(playerTeam,enemyTeam)

k =0
while k==0:
	userInt.MainScreen()
