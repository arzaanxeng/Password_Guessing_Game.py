#Password_Guessing_Game
import random

print("-------- Welcome to Password Guessing Game --------")
print("MODES: EASY | MEDIUM | HARD")

easy_words = ["banana", "car", "aeroplane", "house", "mother"]
medium_words = ["bottle", "blackboard", "cherry", "formula", "planet"]
hard_words = ["avalanche", "diamond", "cosmos", "earth", "mountain"]

user_choice = input("Please enter the difficulty level: ").lower()

if user_choice == "medium":
    password = random.choice(medium_words)
elif user_choice == "hard":
    password = random.choice(hard_words)
else:
    if user_choice != "easy":
        print("Invalid input. Defaulting to EASY mode.")
    password = random.choice(easy_words)

attempts = 0
print(f"\nI'm thinking of a {len(password)} letter word. Good luck!")

while True:
    guess = input("\nEnter your guess: ").lower()
    attempts += 1

    if guess == password:
        print(f"✨ CONGRATULATIONS! You guessed it in {attempts} tries! ✨")
        break

    # Building the hint
    hint = ""
    for i in range(len(password)):
        # Check if the letter matches in the same position
        if i < len(guess) and guess[i] == password[i]:
            hint += guess[i]
        else:
            hint += "_"

    print(f"HINT: {hint}")

print("\n--- GAME OVER ---")
