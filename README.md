# 🎲 Simple Dice Game in Python

This is a simple command-line **Dice Game** built with Python, where **2 to 4 players** compete by rolling a virtual die. The objective is to be the first to reach **50 points**. Each player takes turns rolling the dice, with a twist—rolling a `1` ends the turn with zero points for that round.

## 🎯 Game Rules

- The game supports **2 to 4 players**.
- On their turn, players can choose to:
  - **Roll the die**: Adds a random number (2–6) to the current turn score.
  - **Skip the turn**: Score remains unchanged.
- If the player rolls a `1`:
  - The turn ends immediately.
  - The player scores **0 points** for that round.
- The first player to reach **50 points** wins.

## 🧠 How the Code Works

- Uses the `random` module to simulate dice rolls.
- Loops through players in rounds until someone reaches 50.
- Validates user input for number of players and roll/skip choices.

## 🚀 How to Run

1. Make sure Python is installed (version 3+).
2. Save the code in a file, e.g., `dice_game.py`.
3. Run it using the terminal or command prompt:
   ```bash
   python dice_game.py

Enter the number of players (2 - 4): 2

====== New Round ====

 1 number Turn :
your total score is :  0

Do you want to roll the dice? (y/n): y
you rolled a value 4
your score is :  4
Do you want to roll the dice? (y/n): y
you rolled a value 2
your score is :  6
Do you want to roll the dice? (y/n): n
Player 1 total score is: 6
...


