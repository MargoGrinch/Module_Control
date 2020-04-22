'''
35. Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    n = int(input('size of matrix = '))
    A = np.zeros(n, dtype = int)
            
    for i in range(n):
        A[i] = input()
       
    for i in range(n):
        j = i + 1
        if(A[i] > A[j]):
            print('впорядкована')
            continue
        else:
            print('не впорядкована')
            break
        
    
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
