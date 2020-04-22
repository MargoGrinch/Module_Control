'''
29. Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    i, count = 0, 0
    n = int(input('vvedit k-st elementiv v massive = '))
    a = int(input('chislo dlia porivniannia = '))
    A = np.zeros(n, dtype = int)
    for i in range(n):
        A[i] = input()

    for i in range(n):
        if(A[i] == a):
            break
        elif(A[i] % 2 == 0):
            count += 1
            
    print(f'count = {count}')
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
