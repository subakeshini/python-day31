import random

# Step 1: Define choices
choices = ["rock", "paper", "scissors"]

# Step 2: Get user input
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Step 3: Get computer's random choice
computer_choice = random.choice(choices)

# Step 4: Display computer's choice
print(f"Computer chose: {computer_choice}")

# Step 5: Determine the winner
if user_choice == computer_choice:
    result = "It's a Tie!"
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    result = "You Win!"
elif user_choice in choices:
    result = "You Lose!"
else:
    result = "Invalid input. Please choose rock, paper, or scissors."

# Step 6: Display result
print(result)
