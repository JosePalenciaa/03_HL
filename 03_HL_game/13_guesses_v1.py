end_game = False
while not end_game:

    guess = int_check("Enter your guess: ")

    if guess in already_guessed:
        print(f"You've already guessed {guess}. {guesses_allowed} remaining...")
        continue

    guesses_allowed -= 1
    already_guessed.append(guess)

    if guess == "xxx":
        end_game = True
        break

    elif guess < secret_number:
        print(f"You guessed {guess}.| Too Low! | Guesses left: {guesses_left}")

    elif guess > secret_number:
        print(f"You guessed {guess}.| Too High! | Guesses left: {guesses_left}")

    if guess == secret_number:
        print(f"Congratulations! You found the Secret Number with {guesses_left}")
        rounds_won += 1
        break

    if guesses_allowed == 0:
        print()
        print("Nice Try! You've ran out of guesses.")
        print(f"The Secret Number was {secret_number}")

rounds_played += 1
