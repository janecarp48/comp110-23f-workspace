"""Exercise 3 WHOOP WHOOP!"""

__author__: str = "730555961"


def contains_char(guess: str, character: str) -> bool:
    """Return True if character contained in guess, False if not."""
    assert len(character) == 1
    i: int = 0
    while i < len(guess):
        if guess[i] == character[0]:
            return True
        if guess[i] != character[0] and i == len(guess) - 1:
            return False
        i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Given two strings, return codified emoji string that reflects matching indices."""
    assert len(guess) == len(secret)
    i: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8" 
    resulting_emoji: str = "" 

    while i < len(guess):
        if guess[i] == secret[i]:
            resulting_emoji = resulting_emoji + GREEN_BOX
        elif contains_char(secret, guess[i]) is True:
            resulting_emoji = resulting_emoji + YELLOW_BOX
        else:
            resulting_emoji = resulting_emoji + WHITE_BOX
        i = i + 1
    return resulting_emoji


def input_guess(expected_length: int) -> str:
    """Given an integer, input a guess of the expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    N: int = 0
    has_user_won: bool = False
    while (N < len(secret) + 1) and has_user_won is False:
        print(f"=== Turn {N + 1}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            has_user_won = True
            print(f"You won in {N + 1}/6 turns!")
        else:
            N = N + 1
    if has_user_won is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()