'''
60. Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
однакових чисел, що йдуть підряд в ньому.
'''

import numpy as np

a = np.random.randint(0, 10, 10)

first_array = np.array([a[0] - 1])
second_array = np.array([a[-1] - 1])
conc = np.concatenate((first_array, a, second_array), axis = 0)
cout = 1
c = 1

for i in range(1, len(conc)):
    if conc[i] == conc[i - 1]:
        cout += 1
    else:
        c = cout
        
print(f"Найбільше число однакових чисел, що йдуть підряд в ньому: {c}")
