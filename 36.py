'''
36. Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.

Грінченко Маргарита 122
'''
import numpy as np
while True:
    
    A = np.zeros(10, dtype = int)
            
    for i in range(10):
        A[i] = input(f'{i+1} element = ')

    summa = 0
    for i in range(10):
        if(A[i] > 0):
            summa += A[i]

    print(summa)
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
