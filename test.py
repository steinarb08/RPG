import Creature
import CombatTeam
import Combat
import Ability
import CombatUI
import AbilityEffect
import Item
import Elements
attack = Ability.Ability('Attack',1,1)
effAttack = AbilityEffect.AbilityEffect('basicAttack',0,0,1,1,0)
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


weapon1 = Item.Item('Sword of doom',1)
bonusD = Elements.Elements()
bonusD.SetPhysical(10)
weapon1.SetBonusDamage(bonusD)

c1.EquipItem(weapon1)

print c1.GetItemInSlot(1).GetName()



k =0
while k==0:
	userInt.MainScreen()



