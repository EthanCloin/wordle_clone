from wordle_pkg import word_bank


WORD_BANK = ["crane", "power", 'slice', 'flier', 'eerie',
             "drape", "slime", "brain", "plead", "gnarl"]


def test_generate_word():
    """verify that the generated word is present in the list of valid words"""
    word = word_bank.generate_word()
    assert word in WORD_BANK
