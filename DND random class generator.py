import random
import d20
charnum = 1
check = 0

#stringifier to make roll result readable
class MyStringifier(d20.SimpleStringifier):
    def _stringify(self, node):
        if not node.kept:
            return 'X'
        return super()._stringify(node)

    def _str_expression(self, node):
        return f"{int(node.total)}"

#Lists Classes for convenience
classlist = ["Barbarian", "Cleric", "Druid", "Fighter", "Monk", "Paladin",
             "Sorcerer", "Wizard", "Warlock", "Ranger", "Bard", "Rogue"]
#lists races to print later
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

#class dictionary to avoid having alot of if statements
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

while check == 0:
    timestoloop = input("How many characters do you want to generate? ")
    isint = timestoloop.isdigit()
    isint = str(isint)
    if isint == "True":
        check = 1
    elif isint == "False":
        print("Try again and make sure you entered a number")

check = 0
print("Here are the races you can choose from: ")
print(', '.join(racelist))
while check == 0:
    chosenrace = input("What race do you want to choose? ")
    if chosenrace not in racelist:
        print("Try enter a valid race from the list")
    elif chosenrace in racelist:
        check = 1

check = 0

while check == 0:
    fullconfirm = input("Do you want to create full characters? "
                       "(Gives a random background, random subclass and gives the best skills) ")
    if fullconfirm not in ['yes', 'no']:
        print("This is a yes or no question")
    elif fullconfirm in ['yes', 'no']:
        check = 1

check = 0

while check == 0:
    rollforstats = input(
    "Do you want to roll stats? (Requires D20 to be installed with pip install d20 in cmd) ")
    if rollforstats not in ['yes', 'no']:
        print("This is a yes or no question")
    elif rollforstats in ['yes', 'no']:
        check = 1


timestoloop = int(timestoloop)
for i in range(timestoloop):

    #result list to store dice roll results for later
    resultlist = []

    print("")
    print("Character", charnum)
    charnum = charnum+1

    #randomly chooses class that correlates to the chosen race from the class dictionary from earlier
    def randclass():
        return random.choice(class_dict[chosenrace])

    #code that removes the need for an if statement for every class
    a = randclass()
    print(chosenrace, a)
    b = a.lower()
    if fullconfirm == "yes":
        exec(f"from {b}fullbuild import {b}randsubclass, {b}randbackground, {b}skills")
        exec(f"print({b}randsubclass())")
        exec(f"print({b}randbackground())")
        exec(f"print({b}skills)")
    if rollforstats == "yes":
        for i in range(6):
            result = d20.roll("4d6kh3", stringifier=MyStringifier())
            resultlist.append(str(result))

        print(resultlist)

print("")
input("press enter to end")
