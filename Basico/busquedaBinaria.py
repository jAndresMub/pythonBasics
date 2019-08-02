# -*- coding: utf-8 -*-

mid = 0
val = 0
def binarySearch(numbers, number_to_find, low, high):
    
    global mid 
    global val
    if low > high:
    
        return False
    
    mid = (low + high)/2

    if number_to_find == numbers[mid]:
        val = mid
        return (True)
    
    elif numbers[mid] > number_to_find:

        return binarySearch(numbers, number_to_find, low, mid -1)

    else: 

        return binarySearch(numbers, number_to_find, mid +1, high)

def resultImp(result, val):

    if result is True:
        print('El numero si esta en la lista y su posicion es {}'.format(mid))
    else:
        print('El numero no esta en la lista')



if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]
    number_to_find = int(input('Ingresa un numero: '))

    result = binarySearch(numbers, number_to_find, 0, (len(numbers) -1))

    resultImp(result, val)