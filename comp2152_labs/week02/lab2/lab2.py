import random
weapons = ["Fist","Knife","Club","Gun","Bomb","Nuclear Bomb"]

roll = random.randint(0,5)
heroCombatStrength = 0
heroCombatStrength += roll
print(weapons[roll])

if roll <= 2:
    print("You rolled a weak weapon, friend")
elif roll <= 4:
    print("Your weapon is meh")
else:
    print("Nice weapon,friend")

if roll != 1:
    print("Thank god you didnt roll a fist")