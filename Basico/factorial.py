# -*- coding: utf-8 -*- 

def factorial(number):
    if number > 1:
        number = factorial(number - 1)
    else:
        return number


def run(number):
    input("Ingresa el numero del que quieres saber el factorial")
    if (number > 2):
        factorial(number)
    else:
        print ('{}, debe ser mayor a 2'.format(number))
    print('el factorial es {}'.format(number))
if __name__ == "__main__":

run(number)    