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
    rounds = 3
    wins_p1 = 0
    wins_p2 = 0

    rolls = ["rock", "paper", "scissors"]

    while wins_p1 < rounds and wins_p2 < rounds:

        roll1 = get_roll(player1, rolls)
        roll2 = random.choice(rolls)

        if not roll1:
            print("Try again!")
            continue

        print(f"{player1} rolls {roll1}.")
        print(f"{player2} rolls {roll2}.")

        winner = win_conditions(player1, player2, roll1, roll2)

        if winner is None:
            print("This round was a tie!")
        else:
            print(f"{winner} takes the round!")
            if winner == player1:
                wins_p1 += 1
            elif winner == player2:
                wins_p2 += 1

        print(f"{player1}: {wins_p1} / {player2}: {wins_p2}")
        print()

    if wins_p1 >= rounds:
        overall_winner = player1
    else:
        overall_winner = player2

    print(f"{overall_winner} wins the game!")


def win_conditions(player1, player2, roll1, roll2):
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
    return winner


def get_roll(player_name, rolls):
    print("Available rolls:")
    for index, r in enumerate(rolls, start=1):
        print(f"{index}. {r}")
    print()
    text = input(f"{player_name}, what is your roll: ")
    selected_index = int(text) - 1

    if selected_index < 0 or selected_index >= len(rolls):
        print(f"Sorry {player_name}, {text} is not a valid roll.")
        return None

    return rolls[selected_index]


if __name__ == '__main__':
    main()
