import random

def intro():
    print("🎉 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it in fewer than 10 tries?\n")

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("🚫 Please enter a valid number.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("🔼 Too low!")
        elif guess > number_to_guess:
            print("🔽 Too high!")
        else:
            print(f"✅ Correct! You guessed it in {attempts} tries.")
            break
    else:
        print(f"❌ Game over! The number was {number_to_guess}.")

def main():
    intro()
    play_game()
    while input("\nPlay again? (yes/no): ").lower() == "yes":
        play_game()
    print("👋 Thanks for playing!")

main()
