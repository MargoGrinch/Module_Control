'''
40. Обчислити суму парних елементів одновимірного масиву до першого
зустрінутого нульового елемента.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    n = int(input('number of array = '))
    A = np.zeros(n, dtype = int)

    for i in range(n):
        A[i] = int(input(f'{i+1} element = '))
        
    summa = 0
    for i in range(n):
        if(A[i] % 2 == 0 and A[i] != 0):
            summa += A[i]
        elif (A[i] == 0):
            break
    print(f'summa = {summa}')
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
