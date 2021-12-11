import random

subclasses = ["The Fiend", "The Celestial", "The Genie", "The Great Old One", "The Hexblade",
              "The Undead"]
backgrounds = ["Criminal", "Charlatan", "Guild Artisan", "Sailor", "Urchin"]

warlockrandsubclass = random.choice(subclasses)
warlockrandbackground = random.choice(backgrounds)
warlockskills = ["Deception", "Intimidation"]
if warlockrandsubclass == "Hexblade":
    print("https://arcaneeye.com/class-guides/hexblade-5e-guide/")
    print("Pact of the Blade is best for Hexblade")
