def is_pangram(sentence):
    return len([char for char in set(sentence.lower()) if char.isalpha()]) == 26
