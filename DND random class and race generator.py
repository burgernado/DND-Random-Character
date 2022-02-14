import random
import d20
charnum = 1


class MyStringifier(d20.SimpleStringifier):
    def _stringify(self, node):
        if not node.kept:
            return 'X'
        return super()._stringify(node)

    def _str_expression(self, node):
        return f"{int(node.total)}"


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

timestoloop = int(input("How many characters do you want to generate? "))
fullconfirm = input("Do you want to create full characters? "
                    "(Gives a random background, random subclass and gives the best skills) ")
rollforstats = input(
    "Do you want to roll stats? (Requires D20 to be installed with pip install d20 in cmd) ")

for i in range(timestoloop):

    resultlist = []

    print("")
    print("Character", charnum)
    charnum = charnum+1

    def randclass():
        return random.choice(classlist)

    a = randclass()
    b = a.lower()
    exec(f"randrace = random.choice({b}racelist)")
    print(randrace, a)
    if fullconfirm == "yes":
        exec(f"from {b}fullbuild import {b}randsubclass, {b}randbackground, {b}skills")
        exec(f"print({b}randsubclass)")
        exec(f"print({b}randbackground)")
        exec(f"print({b}skills)")
    if rollforstats == "yes":
        for i in range(6):
            result = d20.roll("4d6kh3", stringifier=MyStringifier())
            resultlist.append(str(result))

        print(resultlist)

print("")
input("press enter to end")
