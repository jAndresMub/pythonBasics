# -*- coding: "utf-8" -*-

divi = 2
final = ""
paraImp = ""

def compVal (numero):
    if numero < 2:
        global paraImp 
        paraImp = "es menor a 2, por definicion no puede ser primo"
        return False
    elif numero > 2:
        return True
    elif numero == 2:
        paraImp = "es Primo"
        return False




def evalNumI(numero):
    global divi
    global final

    for i in range(3, numero-1):
        
        if (numero%i == 0):
            final ="no es Primo"
            break
        else:
            final = "es primo"
    
    return final


def evalNumR(numero):
    global divi
    global final
    if (numero%divi != 0):
        divi = divi + 1
        evalNumR(numero)
    else:
        if(numero == divi):
            final = "es primo"
        else:
            final = "no es primo"
            
    return final

def run():
    global paraImp
    print("E V L U A D O R  D E  N U M E R O S  P R I M O S")
    print("")
    
    numero = int(input("Ingrese el numero a evaluar: "))

    okGo = compVal(numero)

    print("")
    
    opcion = raw_input("Quiere hacerlo Iterativo o Recursivo (max999)? R/I: ")
   
    
    if ((opcion == "R" or opcion == "r") and okGo == True):
        paraImp = evalNumR(numero)
    
    elif ((opcion == "I" or opcion == "i") and okGo == True):
        paraImp = evalNumI(numero)

    
    print ('El numero {}, {}'.format(numero, paraImp))

if __name__ == "__main__":
    run()