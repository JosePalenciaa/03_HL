import random


# Get the secret number
def get_secret_number():

    secret_number = random.randint(1, 100)
    print("The secret number is: ", secret_number)

    get_secret_number()
