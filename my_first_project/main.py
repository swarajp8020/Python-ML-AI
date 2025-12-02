from utils import roll_dice,get_ai_response
if __name__ == "__main__":
    print("--System Starting--")
    print(f"Rolling Dice: {roll_dice(6)}")
    
    user_input = input("Say Something to AI: ")
    reply = get_ai_response(user_input)
    print(f"AI Says: {reply}")