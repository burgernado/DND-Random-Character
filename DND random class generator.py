import random
charnum = 1
classlist = ["Barbarian", "Cleric", "Druid", "Fighter", "Monk", "Paladin",
             "Sorcerer", "Wizard", "Warlock", "Ranger", "Bard", "Rogue"]
racelist = ["Var Human", "Dragonborn", "Half-Elf", "Half-Orc", "Tiefling", "Halfling", "Elf", "Dwarf",
            "Aarakocra", "Warforged", "Aasimar", "Firbolg", "Kenku", "Tortle", "Tabaxi", "Yuan-Ti",
            "Triton", "Satyr", "Changeling", "Kobold", "Owlin", "Bugbear"]

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
owlinclasses = ["Fighter", "Cleric", "Monk", "Druid", "Bard", "Ranger", "Rogue"]
bugbearclasses = ["Fighter", "Ranger", "Rogue"]

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
    "Owlin": owlinclasses,
    "Bugbear": bugbearclasses,
}

timestoloop = int(input("How many characters do you want to generate? "))
print("Here are the races you can choose from:")
print(', '.join(racelist))
chosenrace = input("What race do you want to choose? ")
fullconfirm = input("Do you want to create full characters? "
                    "(Gives a random background, random subclass and gives the best skills) ")

for i in range(timestoloop):

    print("")
    print("Character", charnum)
    charnum = charnum+1

    def randclass():
        return random.choice(class_dict[chosenrace])

    if randclass() == "Barbarian":
        print(chosenrace, "Barbarian")
        print("https://arcaneeye.com/class-guides/5e-barbarian-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/barbarian/")
        if fullconfirm == "yes":
            from barbarianfullbuild import barbrandsubclass, barbrandbackground, barbskills
            print(barbrandsubclass)
            print(barbrandbackground)
            print(barbskills)

    if randclass() == "Druid":
        print(chosenrace, "Druid")
        print("https://arcaneeye.com/class-guides/druid-5e-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/druid/")
        if fullconfirm == "yes":
            from druidfullbuild import druidrandsubclass, druidrandbackground, druidskills
            print(druidrandsubclass)
            print(druidrandbackground)
            print(druidskills)

    if randclass() == "Fighter":
        print(chosenrace, "Fighter")
        print("https://arcaneeye.com/all/dnd-5e-fighter-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/fighter/")
        if fullconfirm == "yes":
            from fighterfullbuild import fighterrandsubclass, fighterrandbackground, fighterskills
            print(fighterrandsubclass)
            print(fighterrandbackground)
            print(fighterskills)

    if randclass() == "Cleric":
        print(chosenrace, "Cleric")
        print("https://arcaneeye.com/class-guides/5e-cleric-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/cleric/")
        if fullconfirm == "yes":
            from clericfullbuild import clericrandsubclass, clericrandbackground, clericskills
            print(clericrandsubclass)
            print(clericrandbackground)
            print(clericskills)

    if randclass() == "Monk":
        print(chosenrace, "Monk")
        print("https://arcaneeye.com/class-guides/5e-monk-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/monk/")
        if fullconfirm == "yes":
            from monkfullbuild import monkrandsubclass, monkrandbackground, monkskills
            print(monkrandsubclass)
            print(monkrandbackground)
            print(monkskills)

    if randclass() == "Paladin":
        print(chosenrace, "Paladin")
        print("https://arcaneeye.com/class-guides/dnd-5e-paladin-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/paladin/")
        if fullconfirm == "yes":
            from paladinfullbuild import paladinrandsubclass, paladinrandbackground, paladinskills
            print(paladinrandsubclass)
            print(paladinrandbackground)
            print(paladinskills)

    if randclass() == "Sorcerer":
        print(chosenrace, "Sorcerer")
        print("https://arcaneeye.com/class-guides/sorcerer-guide-5e/")
        print("https://rpgbot.net/dnd5/characters/classes/sorcerer/")
        if fullconfirm == "yes":
            from sorcererfullbuild import sorcererrandsubclass, sorcererrandbackground, sorcererskills
            print(sorcererrandsubclass)
            print(sorcererrandbackground)
            print(sorcererskills)

    if randclass() == "Wizard":
        print(chosenrace, "Wizard")
        print("https://arcaneeye.com/class-guides/dnd-5e-wizard-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/wizard/")
        if fullconfirm == "yes":
            from wizardfullbuild import wizardrandsubclass, wizardrandbackground, wizardskills
            print(wizardrandsubclass)
            print(wizardrandbackground)
            print(wizardskills)

    if randclass() == "Ranger":
        print(chosenrace, "Ranger")
        print("https://arcaneeye.com/class-guides/bard-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/ranger/")
        if fullconfirm == "yes":
            from rangerfullbuild import rangerrandsubclass, rangerrandbackground, rangerskills
            print(rangerrandsubclass)
            print(rangerrandbackground)
            print(rangerskills)

    if randclass() == "Bard":
        print(chosenrace, "Bard")
        print("https://arcaneeye.com/class-guides/bard-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/bard/")
        if fullconfirm == "yes":
            from bardfullbuild import bardrandsubclass, bardrandbackground, bardskills
            print(bardrandsubclass)
            print(bardrandbackground)
            print(bardskills)

    if randclass() == "Warlock":
        print(chosenrace, "Warlock")
        print("https://arcaneeye.com/all/dnd-5e-warlock-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/warlock/")
        if fullconfirm == "yes":
            from warlockfullbuild import warlockrandsubclass, warlockrandbackground, warlockskills
            print(warlockrandsubclass)
            print(warlockrandbackground)
            print(warlockskills)

    if randclass() == "Rogue":
        print(chosenrace, "Rogue")
        print("https://arcaneeye.com/class-guides/dnd-5e-rogue-guide/")
        print("https://rpgbot.net/dnd5/characters/classes/rogue/")
        if fullconfirm == "yes":
            from roguefullbuild import roguerandsubclass, roguerandbackground, rogueskills
            print(roguerandsubclass)
            print(roguerandbackground)
            print(rogueskills)

print("")
input("press enter to end")
