# -*- coding: utf-8 -*-
# 1)
# Escribir una funcion que dada una cadena y un caracter
# inserte el caracter en la cadena


def separar(cadena, caracter):

    entrega = []

    for letter in cadena:
        entrega.append(letter)
        entrega.append(caracter)
    final = ''.join(entrega)
    print(final)



def run():

    cadena = str(raw_input('Inserte una cadena de strings: '))
    caracter = str(raw_input('ingrese un separador: '))
    separar(cadena, caracter)



if __name__ == "__main__":
    
    run()