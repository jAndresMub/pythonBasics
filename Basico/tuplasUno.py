# -*- coding: utf-8 -*-


#este programa devuelve el primer valor no repetido en una secuencia de caracteres



#se degine la funcion la cual recibe como parametro la cadena de caracteres ingresada por el usuario  
def fNotRepChar(char_sequence):

    #se crea el diccionario seen_letters vacio
    seen_letters ={}

    #este for mira cada uno de los indices (idx) y letras de la cadena de caracteres
    #esto se hace con la funcion enumerate()
    #esta funcion entrega una tupla (Indice, valor en la posicion)
    #por ejemplo en la cadena 'hola' 
    #la funcion enumerate entregaria lo siguiente [(0, h), (1, o), (2, l), (3, 5)]

    for idx, letter in enumerate(char_sequence):
        #si la letra (el valor de letter en el indice idx)
        #no esta en el diccionario seen_letters
        if letter not in seen_letters:
            #agrega la letra (seen_letters[letter]) 
            #en el indice idx y le pone el valor 1
            seen_letters[letter] = (idx, 1)
        else:
            #por el contrario si la letra si esta en el diccionario
            #a la letra en la posicion 0 le suma uno al segundo valor
            #con esto ya se sabe que la letra se ha visto mas de una vez
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1]+1)
    #en esta lista se van a ordenar los valores de las letras vistas

    final_letters = []
    
    #se hace un iteritems para ver los indices y sus valores en el 
    #diccionario seen_letters
    for key, value in seen_letters.iteritems():
    
        if value[1] == 1:
    
            final_letters.append((key, value[0]))

    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'



if __name__ == "__main__":
    #ingreso de la cadena de caracteres
   char_sequence = str(raw_input("Escrube una secuencia de caracteres: "))
   #se llama la funcion fNotRepChar y se guarda el resultado
   #en la variable return
   result = fNotRepChar(char_sequence)

    #si el valor de return es "_" imprime que todos los caracteres se repiten
   if result == '_':
       print('todos los caracteres se repiten')
   #de lo contrario imprime el primer valor no repetido en la cadena de caracteres
   else:
       print('El primer valor no repetido es: {}'.format(result))