

def funcion_decoradora(funcion_parametro):
    #agregando *(nombre, por convencion se pone args)
    #se consigue que la funcion reciba un numero indeterminado de parametros
    #como es el caso de los decoradores, la funcion, no se sabe cuantos
    #y cuales parametros va a recibir. 
    def funcion_interior(*args):
        
        print("vamos a hacer un calculo")
        funcion_parametro(*args)
        print("Terminamos el calculo")

    return funcion_interior


@funcion_decoradora
def suma(num1, num2):
    print (num1 + num2)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

suma(100, 10)
resta(15,1)