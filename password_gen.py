#! /usr/bin/env python

import math
import string
import random


def generatePass(length: int) -> string:
    password = ''
    alpha = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase
    number = string.digits
    for i in range(0, math.ceil(length / 2) - 1):
        password += random.choice(alpha)
        password += random.choice(alpha_upper)
        password += random.choice(number)

    return password.strip()


def main():
    password = generatePass(23)
    print(password)


if __name__ == "__main__":
    main()
