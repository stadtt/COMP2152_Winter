import random


# Dice Options created using list() and range()
diceOptions = list(range(1, 7))

#weapons list
weapons = ["Fist", "Knife", "Club","Gun","Bomb", "Nuclear Bomb"]

print("Available Weapons are:", ', '.join(weapons)  )


def getCombatStrength(prompt):
    while True:
        value = int(input(prompt))
        if 1 <= value <= 6:
            return value
        else:
            print("Invalid Input! Please enter a number between 1 and 6")

combatStrength = getCombatStrength("Please enter a number between 1-6 for Player!")
mCombatStrength = getCombatStrength("Please enter a number between 1-6 for Monster!")

for j in range(1,21,2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll -1]
    monsterWeapon = weapons[monsterRoll -1]

    heroTotal = combatStrength + mCombatStrength
    monsterTotal = combatStrength + mCombatStrength

    print(f"\n Hero Rolled {heroRoll}, Monster Rolled {monsterRoll}")
    print(f"\n Hero Selected {heroWeapon}, Monster selected {monsterWeapon}")
    print(f"\n Hero combatStrength {heroTotal}, Monster combatStrength{monsterTotal}")

    if heroTotal > monsterTotal:
        print("Hero Wins!")
    elif heroTotal < monsterTotal:
        print("Monstr Wins!")
    else:
        print("Its a Tie")

    if j != 11 :
        print("Battle concluded after 20 rounds!")