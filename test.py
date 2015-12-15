import Creature
import CombatTeam
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
