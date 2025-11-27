import random

def start_game():
    print("-------------------------------------------------")
    print("Welcome to the Dockerized Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("-------------------------------------------------")

    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            user_input = input("Enter your guess: ")
            guess = int(user_input)
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    start_game()