# -*- coding: utf-8 -*-

def calculadoraEx(amount):
    mex_to_col = 145.97
    return amount * mex_to_col

def run():
    print('C a l c u l a d o r a  d e  D i v i s a s ')
    print('Convierte pesos Mexicanos a Colombianos')
    print('')

    amount = float(raw_input('Ingresa la cantidad de pesos Mexicanos a convertir: '))

    result = calculadoraEx(amount)

    print('El monto {} de pesos Mexicanos en pesos colombianos es {}'.format(amount, result))
    print('')
if __name__ == "__main__":
    run()