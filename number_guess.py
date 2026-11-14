#This is a number guesser

print("Welcome to the number guesser!")

import random

number = random.randint(1, 100)

choice = 0

while choice != number:
    choice = int(input("Guess a number between 1 and 100: "))
    
    if choice < number:
        print("Too low! Try again.")
    elif choice > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")