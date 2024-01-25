# Change word on a seperate line but in all uppercase

# turn into def print_upper_words

# Change function to only print words with 'e'

# Generalize function to print words that start with certain letters


def print_upper_words(words):
    for xy in words:
        print(xy.upper())

def print_upper_words1(words):
    for xy in words:
        if xy.startswith('e') or xy.startswith('E'):
            print(xy.uppercase())

def print_upper_words2(words):
    for xy in words:
        if xy.startswith('r') or xy.startswith('R') or xy.startswith('b') or xy.startswith('B') or xy.startswith('t') or xy.startswith('T'):
            print(xy.uppercase())
