import random
import sys

first_last = (
    "Liam", "Noah", "Oliver", "Elijah",
    "William", "James", "Benjamin", "Lucas", "Henry", "Alexander",
    "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson",
    "Levi", "Sebastian", "Mateo", "Jack", "Owen"
)

last_last = (
    "Liam", "Noah", "Oliver",
    "Elijah", "William", "James",
    "Benjamin", "Lucas", "Henry", "Alexander",
    "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Levi",
    "Sebastian", "Mateo", "Jack", "Owen"
)

# Generate N random names

for i in range(15):
    fname = random.choice(first_last)
    lname = random.choice(last_last)

    print(f"{fname} {lname}", file=sys.stderr)
