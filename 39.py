'''
39. Дані про температуру повітря і кількості опадів за декаду квітня
зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
вигляді снігу за цю декаду.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    n = int(input('number of array = '))
    A = np.zeros(n, dtype = int)
            
    for i in range(n):
        A[i] = input(f'{i+1} element = ')

    
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
