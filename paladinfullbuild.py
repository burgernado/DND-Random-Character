import random

subclasses = ["Oath of Conquest", "Oath of Glory", "Oath of the Ancients", "Oath of Vengeance"]
backgrounds = ["Sailor", "Soldier", "Faction Agent"]

def paladinrandsubclass():
    return random.choice(subclasses)
def paladinrandbackground():
    return random.choice(backgrounds)
paladinskills = ["Athletics", "Intimidation"]
