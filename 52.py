'''
52. Знайти найбільший елемент з елементів одновимірного масиву, що мають
парний номер. Визначити, чи є він єдиним.
'''

import numpy as np

array = np.random.randint(0, 101, 10)
array = array[array % 2 == 0]
maxim = max(array)
sec = (np.where(array == maxim))[0][0]
array[sec] = min(array)
if max(array) == maxim:
    print("alone")
else:
    print("not alone")
