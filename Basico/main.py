# -*- coding: utf-8 -*-

from lamp import Lamp

def run():
    lamp = Lamp(_is_turned_on = True)

    while True:
        command =  str(raw_input(''' 
        ¿Que deseas hacer?
        [p]render
        [a]pagar
        [s]alir
        '''))
        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_of()
        else:
            break


    


if __name__ == "__main__":
    run()