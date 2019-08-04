# -*- coding: utf-8 -*-

def remp(frase):
    
    sep = frase.split(" ")
    fin = "-".join(sep)
    print(fin)
    

def run():

    frase = str(raw_input('Ingrese una frase: '))
    remp(frase)


if __name__ == "__main__":
    
    run()