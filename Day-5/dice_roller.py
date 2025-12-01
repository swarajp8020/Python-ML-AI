import random
def roll_dice(sides):
    try:
        sides = int(sides)
        if sides <2:
            return "You need at least 2 sides"
        return random.randint(1,sides)
    except ValueError:
        return "Please Enter correct value"
print(roll_dice(6))
print(roll_dice("abc"))
print(roll_dice(1))
