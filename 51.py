'''
51. Дан одновимірний масив а. Сформувати новий масив, який складається
тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
елементів немає, то видати повідомлення.
'''

import numpy as np

a = np.random.randint(0, 201, 10)
a_new = []
for i in range(len(a)):
    if a[i] > i + 10:
        a_new.append(a[i])
a = np.array(a_new)
print(a)

if len(a) == 0:
    print("no such as elements")
