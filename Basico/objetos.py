# -*- coding: utf-8 -*-

# Un mal intento de ascci art
class Lamp:
    _LAMPS = ['''
     
      ' 
 '    |    '
  \       /
    , - .
---(     )---
    \   /
    _|=|_
   |     |
   -------
 ''','''
        
    , - .
   (     )
    \   /
    _|=|_
   |     |
   -------
    ''']
    #Metodo Constructor de la calse
    def __init__(self, _is_turned_on):
        self._is_turned_on = _is_turned_on
    
    def turn_on(self):
        self._is_turned_on = True
        self._display_image()
    
    def turn_of(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])


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