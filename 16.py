'''
16. Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.

Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    i, dob = 0, 1   
    A = np.zeros(15, dtype = int)
    for i in range(15):
        A[i] = randint(10, 50)
        print(A[i])
        if(A[i]%7 == 0):
            dob *= A[i]

    print(f'dob = {dob}')
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
