# Rock, paper, scissors game

import random


def main():
    show_header()

    user = input("Player 1, enter your name: ")
    ai = "Computer"
    play_game(user, ai)


def show_header():
    print("--------------------------------")
    print("   Rock, Paper, Scissors v1")
    print("--------------------------------")


def play_game(player1, player2):
    rolls = ["rock", "paper", "scissors"]

    roll1 = get_roll(player1, rolls)
    roll2 = random.choice(rolls)

    if not roll1:
        print("Can't play that. Exiting...")
        return

    print(f"{player1} rolls {roll1}.")
    print(f"{player2} rolls {roll2}.")

    # Win conditions

    winner = None

    if roll1 == roll2:
        winner = None
    elif roll1 == 'rock':
        if roll2 == 'paper':
            winner = player2
        elif roll2 == 'scissors':
            winner = player1
    elif roll1 == 'paper':
        if roll2 == 'rock':
            winner = player1
        elif roll2 == 'scissors':
            winner = player2
    elif roll1 == 'scissors':
        if roll2 == 'paper':
            winner = player1
        elif roll2 == 'rock':
            winner = player2

    print("The game is over!")

    if winner is None:
        print("It was a tie!")
    else:
        print(f"{winner} takes the game!")


def get_roll(player_name, rolls):
    roll = input(f"{player_name}, enter your roll [rock, paper, scissors]: ")
    roll = roll.lower().strip()
    if roll not in rolls:
        print(f"Sorry {player_name}, {roll} is not a valid roll.")
        return None
    return roll


if __name__ == '__main__':
    main()
