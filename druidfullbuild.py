import random

subclasses = ["Circle of Dreams", "Circle of the Moon", "Circle of Stars"]
backgrounds = ["Acolyte", "Cloistered Scholar",
               "Faction Agent", "Hermit", "Sage", "Urban Bounty Hunter"]

def druidrandsubclass():
    return random.choice(subclasses)
def druidrandbackground():
    return random.choice(backgrounds)
druidskills = ["Insight", "Perception"]
