# -*- coding: utf-8 -*-


def palindrome(word):
    reversed_letters = []

    for letter in word:
        reverse_leters.insert(0, letter)
    
    reversed_word ="".join(reversed_letters)

    if reversed_word == word:
        return True
    else:
        return False



if __name__ == "__main__":
    word = input("Escribe una palabra")
    result = palindrome(word)

    if result:
        print('{}, Si es un palindromo'.format(word))
    else:
        print ('{}, la palabra no es un palindromo')

    