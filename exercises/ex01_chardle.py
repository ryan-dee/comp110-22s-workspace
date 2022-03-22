"""EX01 - Charlde - A cute step toward wordle."""

__author__ = "730464883" 


secret_word: str = (input("Enter a 5-character word:"))
if len(secret_word) != 5:
    print(" Error: Word must contain 5 characters")
    exit()
guess: str = input("Enter a single character: ")
if len(guess) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + guess + " in " + secret_word)


if secret_word[0] == guess:
    print(guess + " found at index 0")
    print 
if secret_word[1] == guess:
    print(guess + " found at index 1")

if secret_word[2] == guess:
    print(guess + " found at index 2")

if secret_word[3] == guess:
    print(guess + " found at index 3")

if secret_word[4] == guess:
    print(guess + " found at index 4")

if secret_word.count(guess) == 1:
    print("1 instance of " + guess + " found in " + secret_word)

if secret_word.count(guess) == 2:
    print("2 instances of " + guess + " found in " + secret_word)

if secret_word.count(guess) == 0:
    print("No instances of " + guess + " found in " + secret_word)

if secret_word.count(guess) == 3:
    print("3 instances of " + guess + " found in " + secret_word)

if secret_word.count(guess) == 4:
    print("4 instances of " + guess + " found in " + secret_word)

if secret_word.count(guess) == 5:
    print("5 instances of " + guess + " found in " + secret_word)