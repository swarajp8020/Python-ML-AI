import random;
def roll_dice(sides):
    try:
        sides= int(sides)
        if sides <2:
            return "You need at least 2 sides."
        return random.randint(1,sides)
    except ValueError:
        return "Enter correct value"
def get_fortune():
    options = [
        "Yes, absolutely.",
        "My sources say no.",
        "Ask again later.",
        "You are destined for greatness.",
        "Focus on your goal."
    ]
    return random.choice(options)