"""Exercise 02 for COMP 110."""

__author__: str = "730555961"

secret_word: str = "python"

guess_word: str = input("What is your 6-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0

resulting_emoji: str = ""

"Concatenating green box if the index of the guess word matches that of the secret word"

while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {len(secret_word)} letters! Try again: ")

while i < len(secret_word):
    if guess_word[i] == secret_word[i]:
        resulting_emoji = resulting_emoji + GREEN_BOX
    else:
        gcharacter_elsewhere: bool = False
        alternate_i: int = 0
        "Checking to see if any characters in the secret word match the specified character of the guess word"
        while (gcharacter_elsewhere is False) and (alternate_i < len(secret_word)):
            if secret_word[alternate_i] == guess_word[i]:
                gcharacter_elsewhere = True
            else:
                alternate_i = alternate_i + 1
        if gcharacter_elsewhere is True:
            resulting_emoji = resulting_emoji + YELLOW_BOX
        else:
            resulting_emoji = resulting_emoji + WHITE_BOX
    i = i + 1
print(resulting_emoji)

if len(guess_word) == 6:
    if guess_word == "python":
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")