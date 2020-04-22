'''
8. Створіть цілочисельний масив А [1..15] за допомогою генератора
випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
найбільший елемент масиву і його індекс.

Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    A = np.zeros((1,15), dtype = int)
    i, j, count = 0, 0, 0

    for i in range(1):
        for j in range(15):
            A[i][j] = randint(-15, 30)            

    print(A)

    maxim = 0
    for i in range(1):
            for j in range(15):
                if(A[i][j] > maxim):
                    maxim = A[i][j]

    print(maxim)
            
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
