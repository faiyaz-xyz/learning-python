import random

tries = 0

guess = 0

while True:
    difficulty = input(
        "What level do you want? (easy, medium, hard, extreme, impossible): "
    )

    if difficulty.lower() == "easy":
        start = 1
        end = 10
        number = random.randint(start, end)
        break
    elif difficulty.lower() == "medium":
        start = 1
        end = 25
        number = random.randint(start, end)
        break
    elif difficulty.lower() == "hard":
        start = 1
        end = 50
        number = random.randint(start, end)
        break
    elif difficulty.lower() == "extreme":
        start = 1
        end = 100
        number = random.randint(start, end)
        break
    elif difficulty.lower() == "impossible":
        start = 1
        end = 1000
        number = random.randint(start, end)
        break
    else:
        print("Select an existing level!")

while guess != number:
    guess = int(input(f"Guess a number between {start} and {end}: "))
    tries += 1

    if guess > end or guess < start:
        print("You cannot guess a number out of range!")
    elif guess > number:
        print("Oh no! It's too high!")
    elif guess < number:
        print("Oh no! It's too low!")
    elif guess == number:
        print(
            f"You guessed it in just {tries} tries! That was {'insane' if tries <= 3 else 'pretty good'} 😎")
        break
