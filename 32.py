'''
32. Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    i, t, count1, count2 = 0, False, 0, 0
    n = int(input('vvedit k-st elementiv v massive = '))
    A = np.zeros(n, dtype = int)
    
    for i in range(n):
        A[i] = input()

    for i in range(n):
        if(A[i] < 0):
            count1 += 1
        elif(A[i] % 2 == 0):       
            count2 += 1

    if(count1 >= 1 and count2 >= 1):
        t = True    

    print(t)
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
