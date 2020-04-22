'''
5. Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази.
Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    A = np.zeros((7,1), dtype = int)
    i, j, summa = 0, 0, 0

    try:
        for i in range(7):
            for j in range(1):
                A[i][j] = randint(0, 8)            
    except ValueError:
        print('only digits')

    print(A)
    
    for i in range(7):
            for j in range(1):
                A[i][j] *= 2

    print(A)
            
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
