'''
10. Дані про температуру повітря за декаду листопада зберігаються в масиві.
Визначити, скільки разів температура опускалася нижче -10 градусів.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    A = np.zeros((1,10), dtype = int)
    i, j, count = 0, 0, 0
    try:
        for i in range(1):
            for j in range(10):
                A[i][j] = int(input())

                    
    except ValueError:
        print('only digits')    

    for i in range(1):
        for j in range(10):
            if(A[i][j] < -10):
                count += 1
    print(count)
            
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
