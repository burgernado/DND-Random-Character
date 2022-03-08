import random
import d20
charnum = 1
check = 0
#this is here to make visual studio not scream at me for not having randrace defined
randrace = ""

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
barbarianracelist = ["Var Human", "Half-Orc", "Half-Elf",
                     "Mountain Dwarf", "Dragonborn", "Tortle", "Warforged"]
fighterracelist = ["Var Human", "Half-Orc", "Feral Tiefling", "Dragonborn",
                   "Mountain Dwarf", "Aarakocra", "Aasimar", "Bugbear", "Kenku", "Kobold", "Leonin",
                   "Tabaxi", "Changeling", "Warforged"]
clericracelist = ["Hill Dwarf", "Var Human", "Half-Elf", "Aarakocra",
                  "Aasimar", "Firbolg", "Kenku", "Tortle", "Warforged"]
sorcererracelist = ["Tiefling", "Half-Elf", "Lightfoot Halfling", "Var Human", "Yuan-Ti Pureblood",
                    "Triton", "Kalashtar", "Warforged", "Satyr", "Eladrin Elf", "Tabaxi", "Changeling"]
monkracelist = ["Wood Elf", "Feral Tiefling", "Var Human", "Stout Halfling",
                "Aarakocra", "Kenku", "Kobold", "Warforged", "Satyr", "Tabaxi"]
paladinracelist = ["Dragonborn", "Half-Elf", "Half-Orc", "Lightfoot Halfling", "Var Human", "Tiefling",
                   "Aasimar", "Kenku", "Tabaxi", "Tortle", "Triton", "Yuan-Ti Pureblood", "Warforged",
                   "Minotaur", "Satyr", "Changeling"]
druidracelist = ["Wood Elf", "Var Human", "Ghostwise Halfling", "Half-Elf",
                 "Aarakocra", "Firbolg", "Kenku", "Tortle", "Warforged"]
wizardracelist = ["High Elf", "Gnome", "Var Human",
                  "Tiefling", "Yuan-Ti Pureblood", "Warforged", "Vedalken"]
bardracelist = ["Half-Elf", "Lightfoot Halfling", "Var Human", "Tiefling", "Eladrin Elf",
                "Tabaxi", "Triton", "Yuan-Ti Pureblood", "Changeling", "Warforged", "Satyr"]
warlockracelist = ["Tiefling", "Lightfoot Halfling", "Half-Elf", "Var Human", "Kobold",
                   "Tabaxi", "Tortle", "Triton", "Yuan-Ti Pureblood", "Verdan", "Warforged", "Satyr"]
rangerracelist = ["Wood Elf", "Stout Halfling", "Var Human", "Aarakocra",
                  "Bugbear", "Kenku", "Kobold", "Tabaxi", "Tortle", "Warforged", "Centaur"]
rogueracelist = ["High Elf", "Wood Elf", "Lightfoot Halfling", "Var Human", "Feral Tiefling", "Aarakocra",
                 "Bugbear", "Kenku", "Kobold", "Tabaxi", "Changeling", "Warforged", "Satyr"]

while check == 0:
    timestoloop = input("How many characters do you want to generate? ")
    isint = timestoloop.isdigit()
    isint = str(isint)
    if isint == "True":
        check = 1
    elif isint == "False":
        print("Try again and make sure you entered a number")

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

    #randomly chooses class from classlist
    def randclass():
        return random.choice(classlist)

    #code that removes the need for an if statement for every class
    a = randclass()
    b = a.lower()
    exec(f"randrace = random.choice({b}racelist)")
    print(randrace, a)
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
