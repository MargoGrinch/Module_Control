'''
13. Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    A = np.zeros((1,15), dtype = int)
    i, j, minim = 0, 0, 0
    try:
        for i in range(1):
            for j in range(15):
                A[i][j] = int(input())
                if(minim > A[i][j]):
                    minim = A[i][j]
    except ValueError:
        print('only digits')    

    print(minim)
            
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
