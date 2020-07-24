# Rock, paper, scissors game

print("--------------------------------")
print("   Rock, Paper, Scissors v1")
print("--------------------------------")

player1 = input("Player 1, enter your name: ")
player2 = input("Player 2, enter your name: ")

rolls = ["rock", "paper", "scissors"]

roll1 = input(f"{player1}, enter your roll [rock, paper, scissors]: ")
roll1 = roll1.lower().strip()
if roll1 not in rolls:
    print(f"Sorry {player1}, {roll1} is not a valid roll.")
roll2 = input(f"{player2}, enter your roll [rock, paper, scissors]: ")
roll2 = roll2.lower().strip()
if roll2 not in rolls:
    print(f"Sorry {player2}, {roll2} is not a valid roll.")

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