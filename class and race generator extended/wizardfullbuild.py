import random

subclasses = ["Bladesinger", "Chronurgy", "Divination", "Evocation"]
backgrounds = ["Acolyte", "Cloistered Scholar", "Sage"]

wizardrandsubclass = random.choice(subclasses)
wizardrandbackground = random.choice(backgrounds)
wizardskills = ["Arcana", "Investigation"]
if wizardrandsubclass == "Bladesinger":
    print("https://arcaneeye.com/class-guides/bladesinger-5e-guide/")
