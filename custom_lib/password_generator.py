# Password generator
import random


def passgen(x):
    password = list()
    password_p1 = list()
    password_p2 = list()
    alphabet = ['a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    special_syms = ['/', '_', '!', '%', '*', '(', ')', '#', '@', '&', ':']


    for i in range(x):
        password_p1.append(random.choice(alphabet))
        password_p2.append(random.randint(1, 9))
        random.shuffle(alphabet)
        password_p1.append(random.choice(special_syms))
        random.shuffle(alphabet)
        random.shuffle(special_syms)

    password.extend(password_p1)
    password.extend(password_p2)
    random.shuffle(password)
    password = [str(i) for i in password]
    password = ''.join(password)
    return password
