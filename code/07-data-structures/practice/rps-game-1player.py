# Rock, paper, scissors game

import random

rolls = {
    'rock': {
        'defeats': ['scissors'],
        'defeated_by': ['paper'],
    },
    'paper': {
        'defeats': ['rock'],
        'defeated_by': ['scissors'],
    },
    'scissors': {
        'defeats': ['paper'],
        'defeated_by': ['rock'],
    },
}


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
    wins = {player1: 0, player2: 0}

    roll_names = list(rolls.keys())

    while find_winner(wins, wins.keys()):

        roll1 = get_roll(player1, roll_names)
        roll2 = random.choice(roll_names)

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


def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name, 0) >= best_of:
            return name

    return None


def win_conditions(player1, player2, roll1, roll2):
    # Win conditions
    winner = None
    if roll1 == roll2:
        print("The play was tied!")

    outcome = rolls.get(roll1, {})
    if roll2 in outcome.get('defeats'):
        return player1
    elif roll2 in outcome.get('defeated_by'):
        return player2

    return winner


def get_roll(player_name, roll_names):
    print("Available rolls:")
    for index, r in enumerate(roll_names, start=1):
        print(f"{index}. {r}")
    print()
    text = input(f"{player_name}, what is your roll [1-3]: ")
    selected_index = int(text) - 1

    if selected_index < 0 or selected_index >= len(roll_names):
        print(f"Sorry {player_name}, {text} is not a valid roll.")
        return None

    return roll_names[selected_index]


if __name__ == '__main__':
    main()
