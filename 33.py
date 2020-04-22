'''
33. Заданий масив А(1:20). Знайти добуток всіх його ненульових елементів.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    i, dob = 0, 1
    A = np.zeros(20, dtype = float)
    
    for i in range(20):
        A[i] = input()

    for i in range(20):
        if(A[i] != 0):
            dob *= A[i]

    print(dob)
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
