import random

# Choices available
choices = ["rock", "paper", "scissors"]

# Computer chooses randomly
computer = random.choice(choices)

# User input
user = input("Enter rock, paper, or scissors: ").lower()

print("Computer chose:", computer)

# Game logic
if user == computer:
    print("It's a tie!")

elif user == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("You lose!")

elif user == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("You lose!")

elif user == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("You lose!")

else:
    print("Invalid input! Please enter rock, paper, or scissors.")