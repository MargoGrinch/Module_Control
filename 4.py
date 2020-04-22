'''
4. Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури.

Грінченко Маргарита 122
'''
import numpy as np
while True:

    A = np.array(['Цеткин', 'Люксембург', 'Санд', 'Стрип', 'Арбатова'])
    letter = input('letter - ')
    print(f'{A} - previous version')

    for i in range(len(A)):
        if (A[i][0] == letter):
            print(A[i])
        else:
            print("NO")

    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
