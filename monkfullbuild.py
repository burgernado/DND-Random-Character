import random

subclasses = ["Way of the Drunken Master", "Way of the Long Death", "Way of the Open Hand"]
backgrounds = ["Urchin", "Criminal"]

def monkrandsubclass():
    return random.choice(subclasses)
def monkrandbackground():
    return random.choice(backgrounds)
monkskills = ["Athletics", "Stealth"]
