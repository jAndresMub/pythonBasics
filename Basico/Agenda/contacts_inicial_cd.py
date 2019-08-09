# -*- coding: utf-8 -*-

class Contact:


    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self.contcts = []
    
    def add(self, name, phone, email):
        print('name: {}, phone: {}, email: {}'.format(name, phone, email))



def run():

    contact_book =ContactBook()


    while True:
        command = str(raw_input('''
            ¿Que deseas hacer?
            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar
            [l]istar
            [s]alir
        '''))

        if command == 'a':
            name = str(raw_input('Ingresa el nombre del contacto: '))
            phone = str(raw_input('Ingresa el numero del contacto: '))
            email = str(raw_input('Ingreas el e-mail del contacto: '))
            
            contact_book.add(name, phone, email)

        elif command =='ac':
            print('actualizar contacto')
        elif command == 'b':
            print('buscar contacto')
        elif command == 'e':
            print('eliminar contacto')    
        elif command == 'l':
            print('listar contactos')
        elif command == 's':
            break
        else:
            print('comando no encontrado')

if __name__ == "__main__":
    run()
