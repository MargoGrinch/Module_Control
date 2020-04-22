'''
41. Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    n = int(input('number of array = '))
    a = int(input('number of maximum = '))
    t = False
    A = np.zeros(n, dtype = int)

    for i in range(n):
        A[i] = int(input(f'{i+1} element = '))

    maximum = 0        
    for i in range(n):
        if(A[i] > maximum):
            maximum = A[i]
    if(maximum <= a):
        t = True
        print(t)
    else:
        print(t)
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
