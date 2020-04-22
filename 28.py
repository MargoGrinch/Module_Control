'''
28. Знайти кількість парних елементів одновимірного масиву.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    i, count = 0, 0
    n = int(input('vvedit k-st elementiv v massive = '))
    A = np.zeros(n, dtype = int)
    for i in range(n):
        A[i] = input()
        if(A[i] % 2 == 0):
            count += 1
            
    print(f'count = {count}')
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
