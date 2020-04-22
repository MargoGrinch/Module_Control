'''
56. Якщо в одновимірному масиві є три поспіль однакових елемента, то
змінній r привласнити значення істина.
'''

import numpy as np

array = np.random.randint(0, 10, 200)
print(array)
r = False
for i in range(len(array) - 2):
    if array[i] == array[i + 1] == array[i + 2]:
        r = True
print(f"r - {r}")
