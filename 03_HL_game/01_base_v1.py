import random


# Checks for valid integer for user guess
def int_check(question, low=1, high=100, exit_code=None):

    if low is None and high is None:
        error = "Please enter a valid integer"
        situation = "any integer"
    elif low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check that integer is valid (i.e., not too low / too high, etc.)
            if situation == "any integer":
                return response

            elif situation == "both" and low <= response <= high:
                return response

            elif situation == "low only" and response >= low:
                return response

            print(error)

        except ValueError:
            print()
            print(error)
            continue


# comparing function...
def compare_numbers(number_secret, user_guess):

    if user_guess < number_secret:
        print("Higher!")
    elif user_guess > number_secret:
        print("Lower!")
    else:
        print("Congratulations! You found the number!")
        return True
    return False


# Display instructions function
def yes_no_why(question):
    while True:
        response = input(question).lower()

        for item in yesno_list:
            if response == item[0] or response == item:
                return item

        print("Please enter a valid response (yes / no / why)")
        print()


yesno_list = ["yes", "no", "why"]


def instructions():
    print("---------------------")
    print("**** How to Play ****")
    print("---------------------")
    print()
    print("The computer will randomly generate a secret number between 1 to 100... "
          "\n- Enter the number of rounds you want to play or <space> for infinite. "
          "\n- You are given 6 guesses. "
          "\n- Guess the secret number. "
          "\n- Can you win?")
    print()


# Introduction / title of game
print("###########################")
print("!!! Higher / Lower Game !!!")
print("###########################")
print()

# Display instructions (yes, no, why)
display_instructions = yes_no_why("Would you like to see instructions (y / n / w)? ")

if display_instructions == "yes":
    print()
    instructions()

elif display_instructions == "why":
    print("😡 BECAUSE I SAID SO 😡\n")
    display_instructions = yes_no_why("Would you like to see instructions (y / n / w)? ")


print("\n===================")
print("!!! Let's Begin !!!")
print("===================\n")

# Generates secret number...
secret_number = random.randint(1, 100)

# Range that secret number is in...
low_number = 1
high_number = 100

max_guess = 6
guesses_allowed = max_guess

# List for already guessed integers
guess = []
already_guessed = []
guesses_left = guesses_allowed

# Rounds mechanics
rounds_played = 0
rounds_won = 0
rounds_lost = 0


rounds = int_check("How many rounds (<enter> for infinite): ", 1, exit_code="xxx")

mode = "regular"

if rounds == "":
    mode = "infinite"

# rounds loop
while True:

    if mode == "infinite":
        print()
        heading = f"Round {rounds_played + 1} of Infinite Mode"
        rounds += 1

    else:
        print()
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1

    end_game = False
    while not end_game:

        guess = int_check("Enter your guess: ")

        if guess in already_guessed:
            print(f"You've already guessed {guess}. {guesses_allowed} guesses remaining...")
            continue
            guesses_left = guess

        guesses_allowed -= 1
        already_guessed.append(guess)

        if guess == "xxx":
            end_game = True
            break

        elif guess < secret_number:
            print(f"You guessed {guess}.| Too Low! | Guesses left: {guesses_left}")
            guesses_left -= 1

        elif guess > secret_number:
            print(f"You guessed {guess}.| Too High! | Guesses left: {guesses_left}")
            guesses_left -= 1

        if guess == secret_number:
            print(f"Congratulations! You found the Secret Number with {guesses_left} guess(es) left.")
            rounds_won += 1
            break

        if guesses_allowed == 0:
            print()
            print("Nice Try! You've ran out of guesses.")
            print(f"The Secret Number was {secret_number}")
            rounds_lost += 1
            break

    rounds_played += 1
