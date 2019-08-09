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

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                break

    def search(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
            else:
                self._not_found(contact)
    
    def _not_found(self, name):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('No encontramos el contacto: {}'.format(contact.name))
                
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
            
            name = str(raw_input('Ingrese el nombre del contacto que quiere buscar: '))
            contact_book.search(name)

        elif command == 'e':
            
            name = str(raw_input('Ingrese el nombre del contacto que quiere eliminar: '))
            contact_book.delete(name)
        
        elif command == 'l':
            
            contact_book._show_all()

        elif command == 's':
            break
        else:
            print('comando no encontrado')

if __name__ == "__main__":
    run()
