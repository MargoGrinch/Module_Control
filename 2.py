'''
2. Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
екран значення коріння і квадратів кожного з елементів масиву.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    x = np.zeros((5,1), dtype = int)
    i, j, summa = 0, 0, 0

    try:
        for i in range(5):
            for j in range(1):
                x[i][j] = int(input())        
    except ValueError:
        print('only digits')

    for i in range(5):
        for j in range(1):
            if(x[i][j] < 0):
                print(f'{x[i][j]} - sqr = {x[i][j]*x[i][j]} - sqrt = have no')
            else:
                print(f'{x[i][j]} - sqr = {x[i][j]*x[i][j]} - sqrt = {x[i][j]**(1/2)}')

    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
