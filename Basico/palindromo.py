# -*- coding: utf-8 -*-


def palindromo(word):
    
    palabraRev = word[::-1]

    print (palabraRev)

    if palabraRev == word:
         print ("Es un palindromo")
       
    else:
         print ("No es un palindromo")

def run():
    word = raw_input("Ingresa una palabra: ")
    palindromo(word)
    

if __name__ == "__main__":
    
    run()

    