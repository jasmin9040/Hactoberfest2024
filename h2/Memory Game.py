import time
import random

def memory_game():
    items = random.sample(range(10, 100), 5)
    print("Remember these numbers:", items)
    time.sleep(3)
    print("\n" * 50)  # Clear the screen
    
    guesses = input("Enter the numbers you remember, separated by spaces: ")
    guessed_items = list(map(int, guesses.split()))
    
    correct = [num for num in guessed_items if num in items]
    print(f"You remembered {len(correct)} correctly:", correct)

memory_game()
