def int_check(question, low=None, high=None, exit_code=None):

    if low is None and high is None:
        error = "Please enter an integer"
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
            print(error)
            continue

# main routine goes here


rounds_played = 0
rounds_won = 0

low_number = 1
high_number = 100

mode = "regular"

rounds = int_check("How many rounds: ", 1, exit_code="")

if rounds == "":
    mode = "infinite"
    rounds = 5

# rounds loop
end_game = False
while not end_game:

    if mode == "infinite":
        heading = f"Round {rounds_played + 1} of Infinite Mode"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1

    # Start Round!!
    while True:
        secret = 7

        guess = int_check("Guess (or 'xxx' to exit): ", low_number, high_number, "xxx")
        print("You guessed", guess)

        if guess == "xxx":
            end_game = True
            break

        # compare guess to the secret number
        print("Pretend we've compared")

        if guess == secret:
            rounds_won += 1
            break

    # check if we are out of rounds
    if rounds_played >= rounds:
        break
