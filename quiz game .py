score = 0

print("===== Simple Quiz App =====")

# Question 1
print("\n1. What is the capital of India?")
print("a) Mumbai")
print("b) Delhi")
print("c) Chennai")

answer = input("Enter your answer: ")

if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
print("\n2. Which language is used for Python programming?")
print("a) Python")
print("b) Java")
print("c) C++")

answer = input("Enter your answer: ")

if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 3
print("\n3. How many days are there in a week?")
print("a) 5")
print("b) 6")
print("c) 7")

answer = input("Enter your answer: ")

if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Final Score
print("\n===== Quiz Finished =====")
print("Your score is:", score, "/ 3")