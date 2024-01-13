import random
import string

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
