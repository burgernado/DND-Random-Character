import random

subclasses = ["Arcane Trickster", "Assassin"]
backgrounds = ["Criminal", "Urchin"]

def roguerandsubclass():
    randclass = random.choice(subclasses)
    if(randclass == "Arcane Trickster"):
        print("You want to make INT your best if you stick with Arcane Trickster");
        print("https://arcaneeye.com/class-guides/arcane-trickster-5e-guide/")  
    return randclass

def roguerandbackground():
    return random.choice(backgrounds)
rogueskills = ["Persuasion", "Perception"]