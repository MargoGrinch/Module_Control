'''
44. Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3.

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
        if(A[i] == (i+1) and A[i] % 3 == 0):
            count += 1
            
    print(count)
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
