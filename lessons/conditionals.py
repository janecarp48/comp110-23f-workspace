

def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    print(my_words) 

def mimic_letter(my_words: str, i: int) -> str:
    if i > len(my_words):
        print("Too high of an index")
    else:
        print(my_words[i])