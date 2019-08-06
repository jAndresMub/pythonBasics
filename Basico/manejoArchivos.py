# -*- coding: utf-8 -*-


def run():
    counter = 0
    with open('alphbet.txt', 'r') as f:
        for line in f:
            counter += line.count('El')
    
    print(counter)




if __name__ == "__main__":
    run()