

def funcion_decoradora(funcion_parametro):
    
    def funcion_interior():
        
        print("vamos a hacer un calculo")
        funcion_parametro()
        print("Terminamos el calculo")

    return funcion_interior


@funcion_decoradora
def suma():
    print (15+20)


def resta():
    print(15-5)

suma()
resta()