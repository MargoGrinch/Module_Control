'''
38. Дані про направлення вітру (північний, південний, східний, західний) і
силі вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув
південний вітер з силою, що перевищує 8 м / с.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    print('1 - північний\n2 - південний\n3 - східний\n4 - західний')
    A = np.zeros((4, 10), dtype = int)

    i = int(input('number of season = '))

    if(i == 1):
        for j in range(10):
            print('північний\n')
            A[i][j] = int(input())
    elif(i == 2):
        for j in range(10):
            print('південний\n')
            A[i][j] = int(input())
    elif(i == 3):
        for j in range(10):
            print('східний\n')
            A[i][j] = int(input())
    elif(i == 4):
        for j in range(10):
            print('західний\n')
            A[i][j] = int(input())
    else:
        print('restart')

    count = 0        
    for i in range(4):
        for j in range(10):
            if(A[2][j] > 8):
                count += 1
            
    print(count)
    
        
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
