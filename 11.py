'''
11. Дані про температуру води на Чорноморському узбережжі за декаду
вересня зберігаються в масиві. Визначити, скільки за цей час було днів, придатних для
купання.

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
            if(A[i][j] > 17):
                count += 1
    print(f'{count} днів - температура >17, отже можна купатись')
            
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
