'''
23. Знайти суму всіх елементів масиву цілих чисел, які менше середнього
арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 150 до 300.

Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    i, summa, summa_rez = 0, 0, 0
    A = np.zeros(20, dtype = int)
    for i in range(20):
        A[i] = randint(150, 300)
        print(A[i])
        summa += A[i]

    for i in range(20):
        if(A[i] < summa/20):
            summa_rez += A[i]

    print(f'summa = {summa_rez}')    
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
