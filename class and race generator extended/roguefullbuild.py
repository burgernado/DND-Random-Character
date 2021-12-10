import random

subclasses = ["Arcane Trickster", "Assassin"]
backgrounds = ["Criminal", "Urchin"]

roguerandsubclass = random.choice(subclasses)
roguerandbackground = random.choice(backgrounds)
rogueskills = ["Persuasion", "Perception"]
if roguerandsubclass == "Arcane Trickster":
    print("You want to make INT your best if you stick with Arcane Trickster")
    print("https://arcaneeye.com/class-guides/arcane-trickster-5e-guide/")
