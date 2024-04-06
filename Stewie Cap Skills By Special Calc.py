base = 50
special = 5
luck = 2
specials = ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]

print("This program can be used to plan a character when using the Stewie Tweaks setting \"Cap Skills By SPECIAL\"\n")

print(f"Skill base: {base}")
print(f"Points added by SPECIAL: {special}")
print(f"Points added by Luck: {luck}\n")

playerSpecial = input("Please input the SPECIAL stat that you want to check: ").lower().capitalize()
valid = 0
while valid == 0:
    if playerSpecial not in specials:
        playerSpecial = input("Invalid SPECIAL stat. Try Again: ").lower().capitalize()
    elif playerSpecial == "Luck":
        playerSpecial = input("Luck affects no skills. Try Again: ").lower().capitalize()
    else:
        valid = 1

playerScore = input("Please input your SPECIAL score: ")
valid = 0
while valid == 0:
    try:
        playerScore = int(playerScore)
        if playerScore < 1 or playerScore > 10:
                playerScore = input("Value must be from 1 to 10. Try again: ")
        else:
            valid = 1
    except ValueError:
        playerScore = input("Input must be an integer. Try again: ")
        
playerLuck = input("Please input your Luck score: ")
valid = 0
while valid == 0:
    try:
        playerLuck = int(playerLuck)
        if playerLuck < 1 or playerLuck > 10:
                playerLuck = input("Value must be from 1 to 10. Try again: ")
        else:
            valid = 1
    except ValueError:
        playerLuck = input("Input must be an integer. Try again: ")
        
result = 50 + ((playerScore * special) + (playerLuck * luck))

if result >100:
    result = 100

print(f"Your maximum value for skills governed by {playerSpecial} is {result}\n")

print(f"Skill(s) goverened by {playerSpecial}:")
if playerSpecial == "Strength":
    print("Melee Weapons.")
if playerSpecial == "Perception":
    print("Energy Weapons, Explosives, Lockpick.")
if playerSpecial == "Endurance":
    print("Survival, Unarmed.")
if playerSpecial == "Charisma":
    print("Barter, Speech.")
if playerSpecial == "Intelligence":
    print("Medicine, Repair, Science.")
if playerSpecial == "Agility":
    print("Guns, Sneak.")
 
print(f"\nWith your current SPECIAL stats, you can get these skills to {result}.")

input()