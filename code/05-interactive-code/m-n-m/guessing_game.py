import random

print("--------------------------------------")
print("          M&M Guessing Game")
print("--------------------------------------")

print("Guess the number of M&Ms and you get lunch on the house!")
print("It is between 1 and 100.")
print()

mm_count = random.randint(1, 100)  # Calls for a random integer between 1 and 100.
attempt_limit = 10
attempts = 0

while attempts < attempt_limit:  # While loop to give user a certain number of attempts.
    guess_text = input("How many M&Ms are in the jar? ")  # reminder: this value is a string
    guess = int(guess_text)  # turns the string above into an integer
    attempts += 1  # keeps track of number of attempts user has made

    if mm_count == guess:
        print(f"Winner! You got free lunch! The number was {guess}. ")
        break  # break disrupts the loop
    elif mm_count < guess:
        print("That's too high.")
    else:
        print("That's too low.")

if mm_count == guess:
    print(f"You completed this in {attempts} attempts.")
else:
    print("Sorry, better luck next time!")



