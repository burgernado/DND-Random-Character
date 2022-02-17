import random

subclasses = ["Abberant Mind", "Draconic Bloodline", "Shadow Magic"]
backgrounds = ["Courtier", "Faction Agent", "Guild Artisan"]

def sorcererrandsubclass():
    return random.choice(subclasses)
def sorcererrandbackground():
    return random.choice(backgrounds)
sorcererskills = ["Arcana", "Persuasion"]
