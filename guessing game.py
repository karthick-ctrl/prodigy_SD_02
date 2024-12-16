import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have picked a random number between 1 and 100. Can you guess what it is?")

    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < target_number:
                print("Too low! Try again.")
            elif user_guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()
