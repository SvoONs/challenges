from data import DICTIONARY, LETTER_SCORES

def load_words() -> list:
    """Load dictionary into a list and return list"""
    with open("dictionary.txt", "r") as f:
        words = f.read().splitlines()
    return words

def calc_word_value(word: str) -> int:
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    for letter in word:
        if letter.isalpha():
            word_value += LETTER_SCORES[letter.upper()]
    return word_value

def max_word_value(words: list = None) -> str:
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    max_value = 0
    for word in words:
        word_value = calc_word_value(word)
        if word_value>max_value:
            max_value = word_value
            max_word_value=word
    return max_word_value



if __name__ == "__main__":
    pass # run unittests to validate
