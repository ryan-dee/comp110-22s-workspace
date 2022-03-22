"""Wordle."""

__author__ = "730464883"


def contains_char(a: str, b: str) -> bool:
    """Returns True if a contained in b."""    
    assert len(b) == 1 
    alt: int = 0
    while alt < len(a):   
        if a[alt] == b:
            return True
        alt = alt + 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Matching Str."""
    assert len(secret) == len(guess)
    result_emoji = ""
    index: int = 0
    while index < len(guess):
        if secret[index] == guess[index]:
            result_emoji = result_emoji + GREEN_BOX
        else:
            test = contains_char(secret, guess[index])      
            if test is True:
                result_emoji = result_emoji + YELLOW_BOX
            if test is False:
                result_emoji = result_emoji + WHITE_BOX
        index = index + 1
    return result_emoji


def input_guess(length: int) -> str:
    """Test the length of guess compared to secret word."""
    guess = input("Enter a 5 character word: ")
    while int(length) != int(len(guess)):  
        guess = input(str("That Wasn't " + str(int(length)) + " chars, try again: "))   
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn_counter: int = 1
    winner: bool = False
    while not winner and turn_counter < 7:
        ((print(f"=== Turn  {turn_counter} /6 ===")))
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            winner = True
            print(f"You won in {turn_counter} turns!")
        else:
            turn_counter = turn_counter + 1  
    if not winner:
        print(str("x/6 Sorry, try again tomorrow"))


if __name__ == "__main__":
    main()

