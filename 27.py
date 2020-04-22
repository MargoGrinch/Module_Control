'''
27. Лінійний масив містить відомості про кількість опадів, що випали за
кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість
опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих
місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.

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
