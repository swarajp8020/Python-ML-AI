import random
def roll_dice(sides):
    try:
        sides=int(sides)
        if sides<2:
                return "You need at least 2 sides"
        return random.randint(1,sides)
    except ValueError:
        return "Plesae write correct value"
    except ZeroDivisionError:
        return "VAlue is invalid"
    except Exception as e:
        return f"Unknow error {e}"
print(roll_dice(6))
print(roll_dice("A"))
print(roll_dice("blbl"))