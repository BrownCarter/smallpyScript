#!/bin/env python3

# user -> u0_a271
# file -> main.py
# date -> Tue-May-2022  12:31:57
def main():
    count = 0
    with open("./employee.tsv", "r") as theFile:
        next(theFile)
        for lines in theFile:
            linex = lines.split()
            firstname = linex[0]
            lastname = linex[1]
            position = linex[2]
            with open("./letter.txt", "r") as letter:
                output = letter.read()
                output = output.replace("{firstname}", firstname)
                output = output.replace("{lastname}", lastname)
                output = output.replace("{position}", position)
            count += 1
            with open(f"output{count}.txt", "w") as final:
                final.write(output)


if __name__ == "__main__":
    main()
