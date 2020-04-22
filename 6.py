'''
6. Створіть масив А [1..8] за допомогою генератора випадкових чисел з
елементами від -10 до 10 і виведіть його на екран. Підрахуйте кількість від’ємних
елементів масиву.

Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    A = np.zeros((8,1), dtype = int)
    i, j, count = 0, 0, 0

    for i in range(8):
        for j in range(1):
            A[i][j] = randint(-10, 10)            

    print(A)
    
    for i in range(8):
            for j in range(1):
                if(A[i][j] < 0):
                    count += 1

    print(count)
            
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
