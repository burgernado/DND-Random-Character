import random
charnum = 1
classlist = ["Barbarian", "Cleric", "Druid", "Fighter", "Monk", "Paladin",
             "Sorcerer", "Wizard", "Warlock", "Ranger", "Bard", "Rogue"]
racelist = ["Var Human", "Dragonborn", "Half-Elf", "Half-Orc", "Tiefling", "Halfling", "Elf", "Dwarf",
            "Aarakocra", "Warforged", "Aasimar", "Firbolg", "Kenku", "Tortle", "Tabaxi", "Yuan-Ti", "Triton",
            "Satyr", "Changeling", "Kobold", "Bugbear", "Gnome", "Leonin", "Minotaur", "Vedalken"]

varhumanclasses = ["Barbarian", "Fighter", "Cleric", "Sorcerer", "Monk",
                   "Paladin", "Druid", "Wizard", "Bard", "Warlock", "Ranger", "Rogue"]
dragonbornclasses = ["Barbarian", "fighter", "Paladin"]
halfelfclasses = ["Barbarian", "Bard", "Warlock"]
halforcclasses = ["Paladin", "Fighter", "Barbarian"]
tieflingclasses = ["Fighter", "Sorcerer", "Monk", "Paladin", "Wizard", "Bard", "Warlock", "Rogue"]
halflingclasses = ["Sorcerer", "Monk", "Paladin", "Druid", "Bard", "Warlock", "Ranger", "Rogue"]
elfclasses = ["Monk", "Druid", "Wizard", "Ranger", "Rogue", "Sorcerer", "Bard"]
dwarfclasses = ["Barbarian", "Fighter", "Cleric"]
aarakocraclasses = ["Fighter", "Cleric", "Monk", "Druid", "Ranger", "Rogue"]
warforgedclasses = ["Barbarian", "Cleric", "Druid", "Fighter", "Monk", "Paladin",
                    "Sorcerer", "Wizard", "Warlock", "Ranger", "Bard", "Rogue"]
aasimarclasses = ["Cleric", "Fighter", "Paladin"]
firbolgclasses = ["Cleric", "Druid"]
kenkuclasses = ["Fighter", "Cleric", "Monk", "Paladin", "Druid", "Ranger", "Rogue"]
tortleclasses = ["Barbarian", "Cleric", "Paladin", "Druid", "Warlock", "Ranger"]
tabaxiclasses = ["Fighter", "Sorcerer", "Monk", "Paladin", "Bard", "Warlock", "Ranger", "Rogue"]
yuantipurebloodclasses = ["Sorcerer", "Paladin", "Wizard", "Bard", "Warlock"]
tritonclasses = ["Sorcerer", "Paladin", "Bard", "Warlock"]
satyrclasses = ["Sorcerer", "Monk", "Paladin", "Bard", "Warlock", "Rogue"]
changelingclasses = ["Fighter", "Sorcerer", "Paladin", "Bard", "Rogue"]
koboldclasses = ["Fighter", "Monk", "Warlock", "Ranger", "Rogue"]
bugbearclasses = ["Fighter", "Ranger", "Rogue"]
gnomeclasses = ["Wizard"]
leoninclasses = ["Fighter"]
minotaurclasses = ["Paladin"]
vedalkenclasses = ["Wizard"]

class_dict = {
    "Var Human": varhumanclasses,
    "Aasimar": aasimarclasses,
    "Dragonborn": dragonbornclasses,
    "Half-Elf": halfelfclasses,
    "Half-Orc": halforcclasses,
    "Tiefling": tieflingclasses,
    "Halfling": halflingclasses,
    "Elf": elfclasses,
    "Dwarf": dwarfclasses,
    "Aarakocra": aarakocraclasses,
    "Warforged": warforgedclasses,
    "Firbolg": firbolgclasses,
    "Kenku": kenkuclasses,
    "Tortle": tortleclasses,
    "Tabaxi": tabaxiclasses,
    "Yuan-Ti": yuantipurebloodclasses,
    "Triton": tritonclasses,
    "Satyr": satyrclasses,
    "Changeling": changelingclasses,
    "Kobold": koboldclasses,
    "Bugbear": bugbearclasses,
    "Gnome": gnomeclasses,
    "Leonin": leoninclasses,
    "Minotaur": minotaurclasses,
    "Vedalken": vedalkenclasses
}

timestoloop = int(input("How many characters do you want to generate? "))
print("Here are the races you can choose from:")
print(', '.join(racelist))
chosenrace = input("What race do you want to choose? ")
fullconfirm = input("Do you want to create full characters? "
                    "(Gives a random background, random subclass and gives the best skills) ")
rollforstats = input(
    "Do you want to roll stats? (Requires D20 to be installed with pip install d20 in cmd) ")

for i in range(timestoloop):

    print("")
    print("Character", charnum)
    charnum = charnum+1

    def randclass():
        return random.choice(class_dict[chosenrace])

    a = randclass()
    print(chosenrace,a)
    b = a.lower()
    if fullconfirm == "yes":
       exec(f"from {b}fullbuild import {b}randsubclass, {b}randbackground, {b}skills")
       exec(f"print({b}randsubclass)")
       exec(f"print({b}randbackground)")
       exec(f"print({b}skills)")
    if rollforstats == "yes":
        from statroller.py import result
        print(result)

print("")
input("press enter to end")
