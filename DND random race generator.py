import random
charnum = 1
classlist = ["Barbarian", "Cleric", "Druid", "Fighter", "Monk", "Paladin",
             "Sorcerer", "Wizard", "Warlock", "Ranger", "Bard", "Rogue"]
barbarianracelist = ["Var Human", "Half-Orc", "Half-Elf",
                     "Mountain Dwarf", "Dragonborn", "Tortle", "Warforged"]
fighterracelist = ["Var Human", "Half-Orc", "Feral Tiefling", "Dragonborn",
                   "Mountain Dwarf", "Aarakocra", "Aasimar", "Bugbear", "Kenku", "Kobold", "Leonin", "Owlin",
                   "Tabaxi", "Changeling", "Warforged"]
clericracelist = ["Hill Dwarf", "Var Human", "Half-Elf", "Aarakocra",
                  "Aasimar", "Firbolg", "Kenku", "Tortle", "Warforged", "Owlin"]
sorcererracelist = ["Tiefling", "Half-Elf", "Lightfoot Halfling", "Var Human", "Tabaxi", "Yuan-Ti Pureblood",
                    "Triton", "Kalashtar", "Warforged", "Satyr", "Eladrin Elf", "Tabaxi", "Changeling"]
monkracelist = ["Wood Elf", "Feral Tiefling", "Var Human", "Stout Halfling",
                "Aarakocra", "Kenku", "Kobold", "Warforged", "Satyr", "Owlin", "Tabaxi"]
paladinracelist = ["Dragonborn", "Half-Elf", "Half-Orc", "Lightfoot Halfling", "Var Human", "Tiefling",
                   "Aasimar", "Kenku", "Tabaxi", "Tortle", "Triton", "Yuan-Ti Pureblood", "Warforged",
                   "Minotaur", "Satyr", "Changeling"]
druidracelist = ["Wood Elf", "Var Human", "Ghostwise Halfling", "Half-Elf",
                 "Aarakocra", "Firbolg", "Kenku", "Owlin", "Tortle", "Warforged"]
wizardracelist = ["High Elf", "Gnome", "Var Human",
                  "Tiefling", "Yuan-Ti Pureblood", "Warforged", "Vedalken"]
bardracelist = ["Half-Elf", "Lightfoot Halfling", "Variant Human", "Tiefling", "Eladrin Elf",
                "Owlin", "Tabaxi", "Triton", "Yuan-Ti Pureblood", "Changeling", "Warforged", "Satyr"]
warlockracelist = ["Tiefling", "Lightfoot Halfling", "Half-Elf", "Var Human", "Kobold",
                   "Tabaxi", "Tortle", "Triton", "Yuan-Ti Pureblood", "Verdan", "Warforged", "Satyr"]
rangerracelist = ["Wood Elf", "Stout Halfling", "Var Human", "Aarakocra",
                  "Bugbear", "Kenku", "Kobold", "Owlin", "Tabaxi", "Tortle", "Warforged", "Centaur"]
rogueracelist = ["High Elf", "Wood Elf", "Lightfoot Halfling", "Var Human", "Feral Tiefling", "Aarakocra",
                 "Bugbear", "Kenku", "Kobold", "Owlin", "Tabaxi", "Changeling", "Warforged", "Satyr"]

timestoloop = int(input("How many characters do you want to generate? "))
fullconfirm = input("Do you want to create full characters? "
                    "(Gives a random background, random subclass and gives the best skills) ")
dndclass = input("What class do you want to be? ")

for i in range(timestoloop):

    print("")
    print("Character", charnum)
    charnum = charnum+1

    if dndclass == "Barbarian":
        barbarianrace = random.choice(barbarianracelist)
        print(barbarianrace, "Barbarian")
        print("https://arcaneeye.com/class-guides/5e-barbarian-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/barbarian/")
        if fullconfirm == "yes":
            from barbarianfullbuild import barbrandsubclass, barbrandbackground, barbskills
            print(barbrandsubclass)
            print(barbrandbackground)
            print(barbskills)

    if dndclass == "Druid":
        druidrace = random.choice(druidracelist)
        print(druidrace, "Druid")
        print("https://arcaneeye.com/class-guides/druid-5e-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/druid/")
        if fullconfirm == "yes":
            from druidfullbuild import druidrandsubclass, druidrandbackground, druidskills
            print(druidrandsubclass)
            print(druidrandbackground)
            print(druidskills)

    if dndclass == "Fighter":
        fighterrace = random.choice(fighterracelist)
        print(fighterrace, "Fighter")
        print("https://arcaneeye.com/all/dnd-5e-fighter-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/fighter/")
        if fullconfirm == "yes":
            from fighterfullbuild import fighterrandsubclass, fighterrandbackground, fighterskills
            print(fighterrandsubclass)
            print(fighterrandbackground)
            print(fighterskills)

    if dndclass == "Cleric":
        clericrace = random.choice(clericracelist)
        print(clericrace, "Cleric")
        print("https://arcaneeye.com/class-guides/5e-cleric-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/cleric/")
        if fullconfirm == "yes":
            from clericfullbuild import clericrandsubclass, clericrandbackground, clericskills
            print(clericrandsubclass)
            print(clericrandbackground)
            print(clericskills)

    if dndclass == "Monk":
        monkrace = random.choice(monkracelist)
        print(monkrace, "Monk")
        print("https://arcaneeye.com/class-guides/5e-monk-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/monk/")
        if fullconfirm == "yes":
            from monkfullbuild import monkrandsubclass, monkrandbackground, monkskills
            print(monkrandsubclass)
            print(monkrandbackground)
            print(monkskills)

    if dndclass == "Paladin":
        paladinrace = random.choice(paladinracelist)
        print(paladinrace, "Paladin")
        print("https://arcaneeye.com/class-guides/dnd-5e-paladin-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/paladin/")
        if fullconfirm == "yes":
            from paladinfullbuild import paladinrandsubclass, paladinrandbackground, paladinskills
            print(paladinrandsubclass)
            print(paladinrandbackground)
            print(paladinskills)

    if dndclass == "Sorcerer":
        sorcererrace = random.choice(sorcererracelist)
        print(sorcererrace, "Sorcerer")
        print("https://arcaneeye.com/class-guides/sorcerer-guide-5e/")
        print("https://rpgbot.net/dnd5/characters/classes/sorcerer/")
        if fullconfirm == "yes":
            from sorcererfullbuild import sorcererrandsubclass, sorcererrandbackground, sorcererskills
            print(sorcererrandsubclass)
            print(sorcererrandbackground)
            print(sorcererskills)

    if dndclass == "Wizard":
        wizardrace = random.choice(wizardracelist)
        print(wizardrace, "Wizard")
        print("https://arcaneeye.com/class-guides/dnd-5e-wizard-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/wizard/")
        if fullconfirm == "yes":
            from wizardfullbuild import wizardrandsubclass, wizardrandbackground, wizardskills
            print(wizardrandsubclass)
            print(wizardrandbackground)
            print(wizardskills)

    if dndclass == "Ranger":
        rangerrace = random.choice(rangerracelist)
        print(rangerrace, "Ranger")
        print("https://arcaneeye.com/class-guides/bard-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/ranger/")
        if fullconfirm == "yes":
            from rangerfullbuild import rangerrandsubclass, rangerrandbackground, rangerskills
            print(rangerrandsubclass)
            print(rangerrandbackground)
            print(rangerskills)

    if dndclass == "Bard":
        bardrace = random.choice(bardracelist)
        print(bardrace, "Bard")
        print("https://arcaneeye.com/class-guides/bard-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/bard/")
        if fullconfirm == "yes":
            from bardfullbuild import bardrandsubclass, bardrandbackground, bardskills
            print(bardrandsubclass)
            print(bardrandbackground)
            print(bardskills)

    if dndclass == "Warlock":
        warlockrace = random.choice(warlockracelist)
        print(warlockrace, "Warlock")
        print("https://arcaneeye.com/all/dnd-5e-warlock-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/warlock/")
        if fullconfirm == "yes":
            from warlockfullbuild import warlockrandsubclass, warlockrandbackground, warlockskills
            print(warlockrandsubclass)
            print(warlockrandbackground)
            print(warlockskills)

    if dndclass == "Rogue":
        roguerace = random.choice(rogueracelist)
        print(roguerace, "Rogue")
        print("https://arcaneeye.com/class-guides/dnd-5e-rogue-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/rogue/")
        if fullconfirm == "yes":
            from roguefullbuild import roguerandsubclass, roguerandbackground, rogueskills
            print(roguerandsubclass)
            print(roguerandbackground)
            print(rogueskills)

print("")
input("press enter to end")
