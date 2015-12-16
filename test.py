import Creature
import CombatTeam
import Ability
import AbilityEffect
x = Creature.Creature("Steinar")
print x.GetMaximumHealth()
print x.GetMaximumInitiative()
print x.GetCurrentHealth()


x.SetCurrentHealth(50)
y = CombatTeam.CombatTeam()

y.AddToTeam(x)

print y.GetHighestHealth()

rawr = y.GetAliveMembers()

for i in range(len(rawr)):
	print rawr[i].GetName()


attack = Ability.Ability("Attack",1,1)
attEffect = AbilityEffect.AbilityEffect('AttackDamage',0,0,10,1)

attack.AddEffect(attEffect)


