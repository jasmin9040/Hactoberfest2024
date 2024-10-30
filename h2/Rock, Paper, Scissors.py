import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    
    if player_choice == computer_choice:
        print(f"Both chose {player_choice}. It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print(f"Player wins! {player_choice} beats {computer_choice}.")
    else:
        print(f"Computer wins! {computer_choice} beats {player_choice}.")

rock_paper_scissors()
