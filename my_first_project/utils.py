# utils.py
import random

def roll_dice(sides):
    try:
        sides = int(sides)
        if sides < 2:
            return "Error: Need 2+ sides"
        return random.randint(1, sides)
    except ValueError:
        return "Error: Invalid input"

def get_ai_response(text):
    # We will fake an AI response for now
    responses = [
        "That is interesting!",
        "Tell me more.",
        "I am just a simple script, but I am learning."
    ]
    return random.choice(responses)