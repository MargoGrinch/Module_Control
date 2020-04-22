'''
43. Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    n = int(input('number of array = '))
    t = False
    a = int(input('a = ')) 
    b = int(input('b = '))
    A = np.zeros(n, dtype = int)

    for i in range(n):
        A[i] = int(input(f'{i+1} element = '))


    for i in range(n):
        if(A[i] % a == 0 and A[i] % b != 0):
            t = True
    print(t)
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
