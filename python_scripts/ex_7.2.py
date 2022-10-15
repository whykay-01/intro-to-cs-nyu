import random

random_value = random.randint(1, 6)
print(random_value)

guess = -1

while guess != random_value:
    guess = input("Please guess the dice value: ")

    if guess.isdigit() == True and int(guess) >= 1 and int(guess) <= 6:
        guess = int(guess)

        if guess == random_value:
            print("Correct guess")
        else:
            print("Wrong guess")
    else:
        print("Error: Your input has to be an integer and between 1 and 6")