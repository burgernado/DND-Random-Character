import random

subclasses = ["Hunter", "Horizon Walker"]
backgrounds = ["Criminal", "Urchin"]

def rangerrandsubclass():
    randclass = random.choice(subclasses)
    if(randclass == "Horizon Walker"):
        print("https://arcaneeye.com/class-guides/horizon-walker-5e-guide/")
    return randclass

def rangerrandbackground():
    return random.choice(backgrounds)
rangerskills = ["Survival", "Perception"]