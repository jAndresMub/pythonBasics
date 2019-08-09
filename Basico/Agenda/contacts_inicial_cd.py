# -*- coding: utf-8 -*-

class Contact:


    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self._contacts = []
    
    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)

    def _show_all(self):

        for contact in self._contacts:
            self._print_contact(contact)

    def _print_contact(self, contact):

        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('E-mail: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')


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
            
            contact_book._show_all()

        elif command == 's':
            break
        else:
            print('comando no encontrado')

if __name__ == "__main__":
    run()
