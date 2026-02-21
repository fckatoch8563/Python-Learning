def play_game():
    print("=" * 40)
    print("Welcome to Rock, Paper, Scissors!")
    print("=" * 40)

    player1_score = 0
    player2_score = 0

    while True:
        print("\nPlayer 1 - Choose (rock/paper/scissors) or 'quit' to exit: ", end="")
        p1_choice = input().lower()

        if p1_choice == "quit":
            break

        if p1_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Try again.")
            continue

        print("Player 2 - Choose (rock/paper/scissors): ", end="")
        p2_choice = input().lower()

        if p2_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Try again.")
            continue

        print(f"\nPlayer 1 chose: {p1_choice}")
        print(f"Player 2 chose: {p2_choice}")

        if p1_choice == p2_choice:
            print("It's a tie!")
        elif (
            (p1_choice == "rock" and p2_choice == "scissors")
            or (p1_choice == "paper" and p2_choice == "rock")
            or (p1_choice == "scissors" and p2_choice == "paper")
        ):
            print("Player 1 wins!")
            player1_score += 1
        else:
            print("Player 2 wins!")
            player2_score += 1

        print(f"\nScore - Player 1: {player1_score} | Player 2: {player2_score}")

    print("\n" + "=" * 40)
    print(f"Final Score - Player 1: {player1_score} | Player 2: {player2_score}")
    if player1_score > player2_score:
        print("Player 1 wins the game! 🎉")
    elif player2_score > player1_score:
        print("Player 2 wins the game! 🎉")
    else:
        print("It's a draw! 🤝")
    print("=" * 40)


play_game()

# With strings (old way):
import os

path = "/Users/fckatoch/projects"
file_path = os.path.join(path, "Environments", "test.py")

if os.path.exists(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    print(f"File path: {file_path}")
    print(content)


# With PosixPath (modern way):
from pathlib import Path

path = Path("/Users/fckatoch/projects")
file_path = path / "Environments" / "test.py"
if file_path.exists():
    content = file_path.read_text()
    print(f"File path: {file_path}")
    print(content)


#################################################################################################


import pandas as pd

# Read a CSV file into a DataFrame
df = pd.read_csv("orders.csv")
# See all columns without truncation
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
print(df)
