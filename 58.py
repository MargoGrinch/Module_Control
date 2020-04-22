'''
58. Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому
повторюється найчастіше число.
'''

import numpy as np

array = np.random.randint(0, 10, 150)
print(f"Array: {array}")
c = 1
while len(array) != 0:
    if len(array[array == array[0]]) > c:
        c = len(array[array == array[0]])

    array = array[array != array[0]]
    print(array)
    
print(f"Times that number repeat: {c}")
