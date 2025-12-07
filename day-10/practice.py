import random
def dice_roller(sides):
    try:
        sides = int(sides)
        if sides > 2:
            return "you need at least 2 sides"
        return random.randint(1,sides)
    except ValueError:
        return "Enter correct value"
def get_fortune():
    option = [
        "safasf",
        "safafa",
        "fasfas",
        "sfafsa",
    ]
    return random.choice(option)