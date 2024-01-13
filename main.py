import random
import string
import sys

"""Module providing functions for generating characters and printing Python version."""

WORD_LENGTH = 18

characters = [string.ascii_letters, string.digits, "!@#$%&"]
chars = []
for clist in characters:
    for item in clist:
        chars.append(item)


def generate_chars():
    """
    Generate a random string of characters.

    Returns:
        str: Random string of characters.
    """
    char_generator = [random.choice(chars)for _ in range(WORD_LENGTH)]
    return ''.join(char_generator)


print(generate_chars())


def print_python_version():
    """
    Print the Python version.

    This function prints the version information of the Python interpreter.
    """
    print(sys.version)


print_python_version()
