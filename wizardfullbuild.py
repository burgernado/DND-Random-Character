import random

subclasses = ["Bladesinger", "Chronurgy", "Divination", "Evocation"]
backgrounds = ["Acolyte", "Cloistered Scholar", "Sage"]

def wizardrandsubclass():
    randclass = random.choice(subclasses)
    if(randclass == "Bladesinger"):
        print("You want to make INT your best if you stick with Arcane Trickster");
        print("https://arcaneeye.com/class-guides/arcane-trickster-5e-guide/")   
    return randclass

def wizardrandbackground():
    return random.choice(backgrounds)
wizardskills = ["Arcana", "Investigation"]