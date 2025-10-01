import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts =0

    print("Welcome to guess a Number")
    print("I have selected a number between 1 and 100")
    print("try to guess it")

    while True:
        player_guess = input("Enter Your Guess: ")

        if not player_guess.isdigit():
             print("Enter a valid number.")
             continue

        player_guess = int(player_guess)
        attempts += 1

        if player_guess < number:
           print("to low try again")
        elif player_guess > number:
             print("to high try again")
        else:
             print(f"congratulations you have guessed the number {number} in {attempts} attempts.")
             break
guess_the_number()