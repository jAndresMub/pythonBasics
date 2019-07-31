# -*- coding: utf-8 -*- 

number = 0

def factorial(number):
    
    if number == 0:
        return 1
    else:
        return number * factorial (number - 1)


def run():
    
    number = input("Ingresa el numero del que quieres saber el factorial: ")
    if (number > 2):
        result = factorial(number)
    else:
        print ('{}, debe ser mayor a 2'.format(number))
    print('el factorial es {}'.format(result))
if __name__ == "__main__":
    
    run()    