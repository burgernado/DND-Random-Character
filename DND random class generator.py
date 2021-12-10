import random
charnum = 1
classlist = ["Barbarian", "Cleric", "Druid", "Fighter", "Monk", "Paladin",
             "Sorcerer", "Wizard", "Warlock", "Ranger", "Bard", "Rogue"]
barbarianracelist = ["Var Human", "Half-Orc", "Half-Elf", "Mountain Dwarf", "Dragonborn"]
fighterracelist = ["Var Human", "Half-Orc", "Feral Tiefling", "Dragonborn", "Mountain Dwarf"]
clericracelist = ["Hill Dwarf", "Var Human", "Half-Elf"]
sorcererracelist = ["Tiefling", "Half-Elf", "Lightfoot Halfling", "Var Human"]
monkracelist = ["Wood Elf", "Feral Tiefling", "Var Human", "Stout Halfling"]
paladinracelist = ["Dragonborn", "Half-Elf", "Half-Orc",
                   "Lightfoot Halfling", "Var Human", "Tiefling"]
druidracelist = ["Wood Elf", "Var Human", "Ghostwise Halfling", "Half-Elf"]
wizardracelist = ["High Elf", "Gnome", "Var Human", "Tiefling"]
bardracelist = ["Half-Elf", "Lightfoot Halfling", "Variant Human", "Tiefling"]
warlockracelist = ["Tiefling", "Lightfoot Halfling", "Half-Elf", "Var Human"]
rangerracelist = ["Wood Elf", "Stout Halfling", "Var Human"]
rogueracelist = ["High Elf", "Wood Elf", "Lightfoot Halfling", "Var Human", "Feral Tiefling"]

varhumanclasses = ["Barbarian", "Fighter", "Cleric", "Sorcerer", "Monk",
                   "Paladin", "Druid", "Wizard", "Bard", "Warlock", "Ranger", "Rogue"]
dragonbornclasses = ["Barbarian", "fighter", "Paladin"]
halfelfclasses = ["barbarian"]

timestoloop = int(input("How many characters do you want to generate? "))

for i in range(timestoloop):

    print("")
    print("Character", charnum)
    charnum = charnum+1

    dndclass = random.choice(classlist)

    if dndclass == "Barbarian":
        barbarianrace = random.choice(barbarianracelist)
        print(barbarianrace, "Barbarian")
        print("https://arcaneeye.com/class-guides/5e-barbarian-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/barbarian/")

    if dndclass == "Druid":
        druidrace = random.choice(druidracelist)
        print(druidrace, "Druid")
        print("https://arcaneeye.com/class-guides/druid-5e-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/druid/")

    if dndclass == "Fighter":
        fighterrace = random.choice(fighterracelist)
        print(fighterrace, "Fighter")
        print("https://arcaneeye.com/all/dnd-5e-fighter-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/fighter/")

    if dndclass == "Cleric":
        clericrace = random.choice(clericracelist)
        print(clericrace, "Cleric")
        print("https://arcaneeye.com/class-guides/5e-cleric-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/cleric/")

    if dndclass == "Monk":
        monkrace = random.choice(monkracelist)
        print(monkrace, "Monk")
        print("https://arcaneeye.com/class-guides/5e-monk-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/monk/")

    if dndclass == "Paladin":
        paladinrace = random.choice(paladinracelist)
        print(paladinrace, "Paladin")
        print("https://arcaneeye.com/class-guides/dnd-5e-paladin-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/paladin/")

    if dndclass == "Sorcerer":
        sorcererrace = random.choice(sorcererracelist)
        print(sorcererrace, "Sorcerer")
        print("https://arcaneeye.com/class-guides/sorcerer-guide-5e/")
        print("https://rpgbot.net/dnd5/characters/classes/sorcerer/")

    if dndclass == "Wizard":
        wizardrace = random.choice(wizardracelist)
        print(wizardrace, "Wizard")
        print("https://arcaneeye.com/class-guides/dnd-5e-wizard-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/wizard/")

    if dndclass == "Ranger":
        rangerrace = random.choice(rangerracelist)
        print(rangerrace, "Ranger")
        print("https://arcaneeye.com/class-guides/bard-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/ranger/")

    if dndclass == "Bard":
        bardrace = random.choice(bardracelist)
        print(bardrace, "Bard")
        print("https://arcaneeye.com/class-guides/bard-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/bard/")

    if dndclass == "Warlock":
        warlockrace = random.choice(warlockracelist)
        print(warlockrace, "Warlock")
        print("https://arcaneeye.com/all/dnd-5e-warlock-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/warlock/")

    if dndclass == "Rogue":
        roguerace = random.choice(rogueracelist)
        print(roguerace, "Rogue")
        print("https://arcaneeye.com/class-guides/dnd-5e-rogue-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/rogue/")

print("")
input("press enter to end")
