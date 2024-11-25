import random

def main():
    level = get_level()
    guess = get_guess_list(level)
    while True:
        user_guess = get_input()
        if user_guess == guess:
            print("Just right!")
            break  # Exit the loop when the correct guess is made
        elif user_guess > guess:
            print("Too large!")
        else:
            print("Too small!")

def get_level():
    while True:
        try:
            level_input = int(input("Level: "))
            if level_input > 0:
                return level_input
        except ValueError:
            pass  # Ignore invalid inputs and prompt again.

def get_input():
    while True:
        try:
            user_guess = int(input("Guess: "))
            return user_guess
        except ValueError:
            pass  # Ignore invalid inputs and prompt again.

def get_guess_list(level):
    return random.randint(1, level)

if __name__ == "__main__":
    main()
