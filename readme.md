# Python Mini Games Collection

This project contains a variety of mini-games coded in Python, perfect for beginner to intermediate programmers. These games include interactive classics such as "Guess the Number," "Rock, Paper, Scissors," and more. The project offers both command-line games and a graphical game using Pygame.

## Games Included

1. **Guess the Number**  
   Try to guess the computer's randomly chosen number between 1 and 100.  
   **Usage:** Run the function `guess_the_number()` to start the game.  
   **Instructions:** Guess a number; the game will tell you if it's too high or too low until you find the correct answer.

2. **Rock, Paper, Scissors**  
   Play a round of Rock, Paper, Scissors against the computer.  
   **Usage:** Run the function `rock_paper_scissors()` to play.  
   **Instructions:** Choose either "rock," "paper," or "scissors" to see if you can beat the computer.

3. **Hangman**  
   Try to guess the letters in a randomly chosen word before running out of attempts.  
   **Usage:** Run the function `hangman()` to start.  
   **Instructions:** Guess letters until you either reveal the word or use up all attempts.

4. **Tic-Tac-Toe**  
   A two-player classic where players take turns placing their symbols on a 3x3 grid.  
   **Usage:** Run the function `tic_tac_toe()` to start the game.  
   **Instructions:** Players take turns to place "X" or "O" on the board, aiming to align three in a row.

5. **Word Scramble**  
   Unscramble a randomly scrambled word to reveal the original.  
   **Usage:** Run the function `word_scramble()` to play.  
   **Instructions:** Type the unscrambled word based on the scrambled version presented.

6. **Dice Roll Simulator**  
   Simulates rolling a dice, with the option to roll multiple times.  
   **Usage:** Run the function `roll_dice()` to start the simulation.  
   **Instructions:** Press Enter to roll the dice and choose whether to roll again.

7. **Memory Game**  
   Test your memory by recalling a sequence of numbers after they're briefly displayed.  
   **Usage:** Run the function `memory_game()` to play.  
   **Instructions:** Memorize the displayed numbers, then try to recall them.

8. **Math Quiz**  
   Answer basic math questions generated randomly to score points.  
   **Usage:** Run the function `math_quiz()` to take the quiz.  
   **Instructions:** Answer five math problems and see your score at the end.

9. **Snake Game** (requires Pygame)  
   Control the snake to eat food and grow, but avoid running into yourself or walls.  
   **Usage:** Requires `pygame`. Run the function `snake_game()` to start.  
   **Instructions:** Use arrow keys to control the snake. The game ends if the snake hits a wall or itself.

## Getting Started

1. Clone this repository:
   git clone https://github.com/your-username/python-mini-games.git
   cd python-mini-games
2. For command-line games, run each Python file individually:
   python game_name.py
3. For the Snake Game
   Install the Pygame library (if not already installed):
   pip install pygame

Then run snake_game.py to play.

## Requirements
Python 3.x is required.
Pygame is required only for the Snake Game:
   pip install pygame
## License
This project is licensed under the MIT License. See the LICENSE file for details.

This README gives a clear overview of each game, instructions for playing, and requirements, making it easy for others to understand and run the code.
