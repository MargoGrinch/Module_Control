'''
9. З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
що протягом цього часу температура знижувалася. Визначте, о котрій годині було
вперше зафіксовано від'ємну температуру.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    A = np.zeros((1,12), dtype = int)
    i, j, count = 0, 0, 8
    try:
        for i in range(1):
            for j in range(12):
                A[i][j] = int(input(f'{count} hours - '))
                if(A[i][j] < 0):
                    print(count)
                    break
                count += 1
    except ValueError:
        print('only digits')    
            
    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
