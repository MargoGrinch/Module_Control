'''
34. Дано два лінійних масиву однакової розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    n = int(input('size of matrix = '))
    A = np.zeros(n, dtype = int)
    B = np.zeros(n, dtype = int)
    C = np.zeros(n, dtype = int)
            
    for i in range(n):
        A[i] = input()

    for i in range(n):
        B[i] = input()

    for i in range(n):
        C[i] = A[i] * B[i]

    print(C)
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
