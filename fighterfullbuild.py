import random

subclasses = ["Cavalier", "Battle Master", "Champion", "Echo Knight", "Eldrich Knight"]
backgrounds = ["Criminal", "Soldier", "Sailor"]

fighterrandsubclass = random.choice(subclasses)
fighterrandbackground = random.choice(backgrounds)
fighterskills = ["Athletics", "Perception"]
if fighterrandsubclass == "Battle Master":
    print("https://arcaneeye.com/class-guides/battle-master-5e-guide/")
if fighterrandsubclass == "Eldrich Knight":
    print("https://arcaneeye.com/class-guides/eldritch-knight-5e-guide/")
