def int_check(question, low=None, high=None, exit_code=None):

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


# Rounds mechanics
rounds_played = 0
rounds_won = 0
rounds_lost = 0

mode = "regular"

rounds = int_check("How many rounds (<enter> for infinite): ", 1, exit_code="xxx")

if rounds == "":
    mode = "infinite"

# rounds loop
end_game = ""
while end_game == "no":

    if mode == "infinite":
        heading = f"Round {rounds_played + 1} of Infinite Mode"
        rounds += 1

    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1
