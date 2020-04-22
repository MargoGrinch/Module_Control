'''
20. Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.

Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    i, summa = 0, 0
    A = np.zeros(20, dtype = int)
    number = int(input('your number = '))
    for i in range(20):
        A[i] = randint(50, 100)
        print(A[i])
        if(A[i] > number):
            summa += A[i]

    print(summa)    
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
