'''
15. Знайти суму парних елементів масиву цілих чисел. Розмірність масиву - 20.
Заповнення масиву здійснити випадковими числами від 100 до 200.

Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    i = 0   
    A = np.zeros(10, dtype = int)
    for i in range(10):
        A[i] = randint(100, 200)
        print(A[i])

    summa = 0
    for i in range(1, 20, 2):
        summa += A[i]

    print(f'sum = {summa}')
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
