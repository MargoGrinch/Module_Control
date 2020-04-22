'''
59. Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
чисел в ньому.
'''

import numpy as np

array = np.random.randint(0, 20, 10)
print(array)

array = np.unique(array)
print(len(array))
