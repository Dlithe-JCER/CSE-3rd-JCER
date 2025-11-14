import random

print("----- Number Guessing Game -----")

secret = random.randint(1, 100)


while True:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess <= 0:
        print("Negative or zero not allowed. Try again.")
        continue

    if guess > secret:
        print("Too HIGH! Try again.")
    elif guess < secret:
        print("Too LOW! Try again.")
    else:
        print(f" Correct! You guessed the number")
        break
