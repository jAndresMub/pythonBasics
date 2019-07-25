# -*-coding: utf-8 -*-

def condif(edad):
        if edad > 18:
            resultado = 'es mayor de edad'
            
        else:
            resultado = 'es menor de edad'
            
        return resultado

def func():

    nombre = (raw_input('Ingresa el Nombre: '))
    print('')
    edad = (int(input('Ingresa la edad a consultar: ')))
    print('')
    resultado = condif (edad)
    print ('{} {}'.format(nombre, resultado))


if __name__ == "__main__":
    func()