# -*- coding: utf-8 -*-

# se define el diccionario con la letra como llave y la codificacion
# de dicha letra como el valor
KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def cypher(message):
    #el procedimiento es similar al de la decodificacion
    #sino que en vez de buscar en el diccionaria cada valor
    #se busca es cada llave y se adiciona el valor a la nueva variable
    words = message.split(' ')
    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)

    return ' '.join(cypher_message)

# se define la funcion para decodificar el mensaje
def decipher(message):
    #Crea una lista llamada words, donde cada elemento corresponde a
    # una palabra, ka cual fue encontrada por cada espacio.
    #split lo que hace es que separa cada vez que encuentra un espacio
    #en este caso, si en vez de espacio se pusiera un asterisco
    #separaria cada vez que encontrara un asterisco
    
    words = message.split(' ')
    
    #se genera una lista vacia
    decipher_message = []

    # Por cada palabra en la lista words se hace el bloque de codigo
    for word in words:
        #a la lista vacia se le asigna nada
        decipher_word = ''
        #por cada letra en cada palabra se ejecuta el bloque de codigo
        for letter in word:
            #este for utiliza una tupla (key y value) y evalua los valores
            # de el diccionario KEYS usando iteritems, que devuelve la 
            #llave y el valor
            #este for recorre el diccionario
            for key, value in KEYS.iteritems():
                #si el valor de la letra correspondiente es igual a la letra
                # a la lista se le suma (agrega) la llave
                if value == letter:
                    decipher_word += key
        #lo que se hizo hasta este punto fue evaluar cada letra que 
        #corresponde a un valor del diccionario, cuando se encontrara ese valor
        #en el diccionario a la variable decipher_word se le suma
        #la llave, ya que se esta decodificando el mensaje
        #en la siguiente linea lo que se hace es el append a la lista
        #decipher_message la palabra que la se decodifico
        decipher_message.append(decipher_word)
    #finalmente se devuelve la union de todas las palabras
    #separadas por espacios
    return ' '.join(decipher_message)


def run():

    while True:
#imprime en la consola la interfas grafica
        command = str(raw_input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptograf�a. �Qu� deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))
#inicia con c para codificar
        if command == 'c':
            message = str(raw_input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)
#con d decodifica
        elif command == 'd':
            message = str(raw_input('Escribe tu mensaje tu cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)
#con s sale del programa
        elif command == 's':
            print('salir')
#cualquier otra letra muestra un error
        else:
            print('�Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()