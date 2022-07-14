#!/bin/env python
import cProfile


def main():
    with open('dict.txt', 'r', encoding='UTF-8') as a_dict:
        word = set(a_dict.read().strip().split())
    palindroms = set()
    for palindrom in word:
        if len(palindrom) > 1 and palindrom == palindrom[::-1]:
            palindroms.add(palindrom)
    print(palindroms)


if __name__ == "__main__":
    #    cProfile.run('main()')
    main()
