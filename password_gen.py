#! /usr/bin/env python
""" System modules """
import math
import string
import secrets


def generate_pass(length: int) -> string:
    """
    Function to generate password of length N
    Return password: string
    """

    password: string = ''
    alpha: string = string.ascii_lowercase
    alpha_upper: string = string.ascii_uppercase
    number: int = string.digits
    for _i in range(0, math.ceil(length / 2) - 1):
        password += secrets.choice(alpha)
        password += secrets.choice(alpha_upper)
        password += secrets.choice(number)

    return password.strip()


def main():
    """ Takes a string and run function to generate password of length n """
    password: string = generate_pass(23)
    print(password)


if __name__ == "__main__":
    main()
