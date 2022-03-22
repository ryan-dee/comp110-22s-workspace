"""An example of conditional (if-else) statements."""

import secrets


SECRET: int = 3

print ("I'm thinking of a nuber between 1-5, what is it?")
guess: int = int (input ("What is your guess?"))

if guess == SECRET: 
    print("Youg guessed correctly!!!")
    print("Have a wonderful day!!!")
else:  
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed too high")
    else:
        print("You guessed too low!")

print("Game Over.")  
