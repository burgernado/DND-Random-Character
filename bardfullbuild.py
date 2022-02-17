import random

subclasses = ["College of Eloquence", "College of Lore"]
backgrounds = ["Criminal", "Guild Artisan", "Sailor", "Spy", "Urchin"]

def bardrandsubclass():
    return random.choice(subclasses)
def bardrandbackground():
    return random.choice(backgrounds)
bardskills = ["Deception", "Persuasion"]
