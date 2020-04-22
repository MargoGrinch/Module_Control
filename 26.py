'''
26. Напишіть програму аналізу значень температури хворого за добу:
визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
температури виробляються шість раз на добу і результати вводяться з клавіатури у
масив T.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    i, maximum, summa = 0, 0, 0
    T = np.zeros(6, dtype = int)
    for i in range(6):
        T[i] = input()
        summa += T[i]

    for i in range(6):
        if(maximum < T[i]):
            maximum = T[i]
            
    print(f'maximum = {maximum}\nseredne_znachennia = {summa/6}')
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
