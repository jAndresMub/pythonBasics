# -*- coding: utf-8 -*-

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}
def run():
    while True:
        country = str(raw_input('ingresa el nombre de un pais')).lower()
        try:
            print('la poblacion de {} es: {} millones'.format(country, countries[country]))
        except KeyError:
            print('No tenemos el dato de la poblacion del pais que nos diste {}'.format(country))
if __name__ == "__main__":
  run()  