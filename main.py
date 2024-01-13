import random
import string

word_lenght = 18

characters = [string.ascii_letters, string.digits, "!@#$%&"]
chars = []
for clist in characters:
    for item in clist:
        chars.append(item)


def generate_password():
    password = []
    for i in range(word_lenght):
        rchar = random.choice(chars)
        password.append(rchar)

    return ''.join(password)


print(generate_password())
