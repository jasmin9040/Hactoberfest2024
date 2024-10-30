import random

def roll_dice():
    while True:
        input("Press Enter to roll the dice...")
        print("You rolled a", random.randint(1, 6))
        if input("Roll again? (y/n): ").lower() != 'y':
            break

roll_dice()
