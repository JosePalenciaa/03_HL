
# Compare the secret number to the user's input
def compare_numbers(number_secret, user_guess):

    if user_guess < number_secret:
        print("Higher!")
    elif user_guess > number_secret:
        print("Lower!")
    else:
        print("Congratulations! You found the number!")
        return True
    return False
# 69 is used for testing purposes


secret_number = 69

# Ask the user for their guess
guess = int(input("Enter your guess: "))

# Call the compare_numbers function and store the result
result = compare_numbers(secret_number, guess)

# Display the result
if result:
    print("Good Job!")
else:
    print("Unlucky!")