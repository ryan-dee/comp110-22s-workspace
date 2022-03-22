"""One Shot Wordle."""

__author__ = "730464883"

secret_word = str("python")

guess = str(input("What is your 6-letter guess? "))

while len(str(guess)) != len(str(secret_word)):
    guess = (input("That was not 6 letters! Try again: "))

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result_emoji: str = ""
i: int = 0
while i < len(secret_word):
    if secret_word[i] == guess[i]:
        result_emoji = result_emoji + GREEN_BOX
    else:
        test: bool = False
        alt: int = 0
        while test is not True and alt < len(secret_word):
            if secret_word[alt] == guess[i]:
                test = True
            alt = alt + 1
        if test is True:
            result_emoji = result_emoji + YELLOW_BOX
        else:
            result_emoji = result_emoji + WHITE_BOX
    i = i + 1

if str(result_emoji) == str("🟩🟩🟩🟩🟩🟩"):
    print(result_emoji)
    print("Woo! You got it!")
else:
    print(result_emoji)
    print("Not quite. Play again soon!")
