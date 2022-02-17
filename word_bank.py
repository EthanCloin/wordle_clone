import random


def generate_word():
    """return a random word from the defined list of 10
    Eventually should refactor to use some kind of Dictionary.com API
    """
    valid_words = ["crane", "power", 'slice', 'flier', 'eerie',
                   "drape", "slime", "brain", "plead", "gnarl"]

    return random.choice(valid_words)


print(generate_word())
print(generate_word())
print(generate_word())
