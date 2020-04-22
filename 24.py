'''
24. Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
числами від 500 до 1000.

Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    i, summa = 0, 0
    A = np.zeros(30, dtype = int)
    for i in range(30):
        A[i] = randint(500, 1000)
        print(A[i])
        if(A[i] % 5 == 0 and A[i] % 8 == 0):
            summa += A[i]

    print(f'summa = {summa}')    
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
