import random
# Simple Dice Game

# This is a simple dice game where players take turns rolling a die.# The first player to reach a score of 50 wins.
# If a player rolls a 1, they lose their turn and score 0 for that turn.
# Players can choose to skip their turn by entering 'n'.
def roll_dice():
        min_value = 1
        max_value = 6
        value = random.randint(min_value, max_value)
        return value


# number of players taking input from user
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit() :
        if 2 <= int(players) <= 4:
            players = int(players)
            break
        else:
            print("Please enter a number between 2 and 4.")

    else:
        print("Please enter a valid number.")   

# Initialize player scores

max_score = 50
player_scores = [0 for _ in range(players)]

# main Game loop
while max(player_scores) < max_score:
    print("\n====== New Round ====")

    for player_idx in range(int(players)):             ## loop through each player
        player = input(f"\n {player_idx+1} number Turn : ")
        print("your total score is : ", player_scores[player_idx],"\n")
        current_score = 0

        while True:
            should_roll = input("Do you want to roll the dice? (y/n): ").strip()

            if should_roll.lower() != 'y':
                    print("you skipped your turn")
                    break

            Value = roll_dice()

            if Value == 1:
                print("You loose your turn and score 0")
                Value = 0
                break
            else:
                current_score += Value
                print("you rolled a value", Value)
            
            print("your score is : ", current_score)
        player_scores[player_idx] += current_score
        print(f"Player {player_idx + 1} total score is: {player_scores[player_idx]}")

# Check for a winner
max_score = max(player_scores)
winner = player_scores.index(max_score)
print(f"\n Player {winner + 1} wins with a score of {max_score}")
print("Game Over!")




            
            


