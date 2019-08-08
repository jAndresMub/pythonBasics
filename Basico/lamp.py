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


