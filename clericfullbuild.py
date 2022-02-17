import random

subclasses = ["Forge Domain", "Life Domain", "Light Domain", "Trickery Domain", "War Domain"]
backgrounds = ["Acolyte", "Faction Agent", "Hermit"]

def clericrandsubclass():
    return random.choice(subclasses)
def clericrandbackground():
    return random.choice(backgrounds)
clericskills = ["Insight", "Medicine"]
