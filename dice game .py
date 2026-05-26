import random

print("===== Dice Rolling Simulator =====")

while True:
    dice = random.randint(1, 6)

    print("You rolled:", dice)

    choice = input("Roll again? (yes/no): ")

    if choice.lower() != "yes":
        print("Game ended.")
        break