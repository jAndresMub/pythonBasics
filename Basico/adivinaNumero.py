# -*- coding: utf-8 -*-

from random import randint, uniform,random

def compNum(numFin):
    numIni = int(input("Adivina el Numero, digita uno: "))
    while numFin != numIni:
        
        if (numIni > numFin):
            print("No acertaste, el numero a adivinar es menor")
        else:
            print("No acertaste, el numero a adivinar es mayor")

        numIni = int(input("Intenta de nuevo digita otro numero: "))
    

def genNum():
    return randint(1,100)


def run():
    print ("Vamos a comenzar, tienes que adivinar un numero del 1 al 100 ")
    numFin = genNum()
    compNum(numFin)
    print("Felicitaciones acertaste!!!") 





if __name__ == "__main__":
    run ()