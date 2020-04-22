'''
19. Знайти суму всіх елементів масиву цілих чисел що задовольняють умові:
остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 200 до 300.

Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    i, summa = 0, 0
    A = np.zeros(20, dtype = int)
    for i in range(20):
        A[i] = randint(200, 300)
#        print(A[i])
        if(A[i] % 2 == 3):
            summa += A[i]

    print(summa)    
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
