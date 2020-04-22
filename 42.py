'''
42. Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!

Грінченко Маргарита 122
'''
import numpy as np
while True:

    n = int(input('number of array = '))
    A = np.zeros(n, dtype = int)

    for i in range(n):
        A[i] = int(input(f'{i+1} element = '))

    count = 0
    for i in range(n):
        if(i*i < A[i] and A[i] < i):
            count += 1
    print(count)
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
