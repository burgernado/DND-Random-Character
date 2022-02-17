import random

subclasses = ["Cavalier", "Battle Master", "Champion", "Echo Knight", "Eldrich Knight"]
backgrounds = ["Criminal", "Soldier", "Sailor"]

def fighterrandsubclass():
    randclass = random.choice(subclasses)
    if(randclass == "Battle Master"):
        print("https://arcaneeye.com/class-guides/battle-master-5e-guide/")
    if(randclass == "Eldrich Knight"):
        print("https://arcaneeye.com/class-guides/eldritch-knight-5e-guide/")   
    return randclass

def fighterrandbackground():
    return random.choice(backgrounds)
fighterskills = ["Athletics", "Perception"]