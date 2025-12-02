import random
def roll_dice(sides):
    try:
        sides = int(sides)
        if sides > 2:
            return "you need atleast 2 sides"
        return random.randint(1,sides)
    except ValueError:
        return "Write Proper number"
    except ZeroDivisionError:
        return "Number is Invalid"
    except Exception as e:
        return f"Unknown error {e}"
print(roll_dice(5))