# Functions...
def yes_no_why(question):
    while True:
        response = input(question).lower()

        for item in yesno_list:
            if response == item[0] or response == item:
                return item


yesno_list = ["yes", "no", "why", "xxx"]


def instructions():
    print("**** How to Play ****")
    print()
    print("The computer will randomly generate a secret number between 1 to 100... "
          "\n- your are given 6 guesses. "
          "\n- Enter the number of rounds you want to play or <space> for infinite. "
          "\n- Guess the secret number.")
    print()

# Main routine goes here...


display_response = ""
while display_response != "xxx":

    display_response = yes_no_why("Have you played before? ")

    if display_response == "no":
        print()
        instructions()

    elif display_response == "why":
        print("Because I said so!!!\n")

    else:
        print("program continues")
