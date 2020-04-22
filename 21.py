'''
21. Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
від 50 до 100.

Грінченко Маргарита 122
'''
from random import randint
import numpy as np
while True:

    i, dob = 0, 1
    A = np.zeros(10, dtype = int)
    number = int(input('your number = '))
    for i in range(10):
        A[i] = randint(50, 100)
#        print(A[i])
        if(A[i] < number):
            dob *= A[i]

    print(f'dobutok = {dob}')    
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
