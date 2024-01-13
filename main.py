import random
import string
"""Module providing a function printing python version."""
import sys


WORD_LENGHT = 18

characters = [string.ascii_letters, string.digits, "!@#$%&"]
chars = []
for clist in characters:
    for item in clist:
        chars.append(item)


def generate_chars():
    char_generator = []
    for rchar in range(WORD_LENGHT):
        rchar = random.choice(chars)
        char_generator.append(rchar)

    return ''.join(char_generator)


print(generate_chars())


def print_python_version():
    print(sys.version)


print_python_version()
