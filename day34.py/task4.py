import random

def number_guessing_game():
    secret_number = random.randint(1, 20)
    attempts = 5

    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")

    while attempts > 0:
        try:
            guess = int(input(f"\nYou have {attempts} attempts left. Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        if guess == secret_number:
            print("🎉 Congratulations! You guessed the correct number!")
            break
        elif guess > secret_number:
            print("📉 Too high! Try again.")
        else:
            print("📈 Too low! Try again.")

        attempts -= 1

        if attempts == 0:
            print(f"\n❌ Out of attempts! The correct number was {secret_number}.")

# Run the game
number_guessing_game()
