'''
45. Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
яка містить довжини опор, які встановлюються через кожні R / 5 м.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    n = int(input('number of array = '))
    R = int(input('R = '))

    for i in range(n):
        print(f'{i+1} - {R*3.14}')
        R /= 5
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
