'''
7. Створіть масив А [1..12] за допомогою генератора випадкових чисел з
елементами від -20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи
масиву числом 0.

Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    A = np.zeros((1,12), dtype = int)
    i, j, count = 0, 0, 0

    for i in range(1):
        for j in range(12):
            A[i][j] = randint(-20, 10)            

    print(A)
    
    for i in range(1):
            for j in range(12):
                if(A[i][j] < 0):
                    A[i][j] = 0

    print(A)
            
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
