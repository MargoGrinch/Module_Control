'''
22. Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
Заповнення масиву здійснити випадковими числами від 5 до 500.

Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    i, dob = 0, 1
    A = np.zeros(10, dtype = int)
    for i in range(10):
        A[i] = randint(5, 500)
        print(A[i])
        if(A[i] % 9 == 0):
            dob *= A[i]

    print(f'dobutok = {dob}')    
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
