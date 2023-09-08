#!/bin/env python
""" system module """
import cProfile


def main():
    """Converts sentence to Pig Latin"""
    vowel = {"a", "e", "i", "o", "u"}
    word = input("Enter sentence: ")
    ans = str()
    for pig in word.split():
        pig_latin = pig
        if pig[0].lower() not in vowel:
            pig_latin = pig_latin[1:]
            pig_latin = pig_latin + pig[0]
            pig_latin = pig_latin + "ay"
            ans = ans + pig_latin + " "
        elif pig[0].lower() in vowel:
            pig_latin = pig_latin + "way"
            ans = ans + pig_latin + " "
    print(ans.strip())


if __name__ == "__main__":
    cProfile.run("main()")
