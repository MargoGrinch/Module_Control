'''
12. Дані про температуру повітря за декаду грудня зберігаються в масиві.
Визначити, скільки раз температура була вище середньої за цю декаду.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    A = np.zeros((1,10), dtype = int)
    i, j, count, summa = 0, 0, 0, 0
    try:
        for i in range(1):
            for j in range(10):
                A[i][j] = int(input())
                summa += A[i][j]
    except ValueError:
        print('only digits')    

    for i in range(1):
        for j in range(10):
            if(A[i][j] > (summa/10)):
                count += 1
    print(count)
            
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
