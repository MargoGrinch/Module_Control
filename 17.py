'''
17. Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100
до 200.

Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    i = 0  
    A = np.zeros(20, dtype = float)
    for i in range(20):
        A[i] = randint(100, 200)
        print(A[i])
        
    summa = 0
    for i in range(0, 20, 2):
        summa += A[i] 

    print(f'summa = {summa}')
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
