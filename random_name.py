#!/bin/env python

import random
import sys


def main():
    first_last = (
        "Liam",
        "Noah",
        "Oliver",
        "Elijah",
        "William",
        "James",
        "Benjamin",
        "Lucas",
        "Henry",
        "Alexander",
        "Mason",
        "Michael",
        "Ethan",
        "Daniel",
        "Jacob",
        "Logan",
        "Jackson",
        "Levi",
        "Sebastian",
        "Mateo",
        "Jack",
        "Owen",
    )

    last_last = (
        "Liam",
        "Noah",
        "Oliver",
        "Elijah",
        "William",
        "James",
        "Benjamin",
        "Lucas",
        "Henry",
        "Alexander",
        "Mason",
        "Michael",
        "Ethan",
        "Daniel",
        "Jacob",
        "Logan",
        "Jackson",
        "Levi",
        "Sebastian",
        "Mateo",
        "Jack",
        "Owen",
    )

    # Generate N random names

    for _i in range(15):
        fname = random.choice(first_last)
        lname = random.choice(last_last)

        print(f"{fname} {lname}", file=sys.stderr)


if __name__ == "__main__":
    main()
