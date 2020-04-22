'''
25. Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
100.

Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    i, dob = 0, 1
    A = np.zeros(10, dtype = int)
    for i in range(10):
        A[i] = randint(10, 100)
        print(A[i])
        if(A[i] % 5 == 0):
            dob *= A[i]

    print(f'dobutok = {dob}')    
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
