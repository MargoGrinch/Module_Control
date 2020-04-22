'''
31. Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    i, summa, count = 0, 0, 0
    n = int(input('vvedit k-st elementiv v massive = '))
    A = np.zeros(n, dtype = int)
    
    for i in range(n):
        A[i] = input()

    for i in range(n):
        if(A[i] >= -2 and A[i] <= 10):       
            summa += A[i]
            count +=1

    print(f'{summa/count}')
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
