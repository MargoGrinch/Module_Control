'''
1. Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
один рядок через кому. Отримайте для масиву середнє арифметичне.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    x = np.zeros((5,1), dtype = int)
    i, j, summa = 0, 0, 0
    
    try:
        for i in range(5):
            for j in range(1):
                x[i][j] = int(input())
                summa += x[i][j]        
    except ValueError:
        print('only digits')

            
    print(x[0][0], ",", x[1][0], ",", x[2][0], ",", x[3][0], ",", x[4][0])
            
    print(f'middle rez = {summa/5}')    

    
    
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
