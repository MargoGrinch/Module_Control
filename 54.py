'''
54. Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
однаковими значеннями.
'''

import random

array = []

for i in range(20):
    while True:
        try:
            num = int(input("Your number: "))
            break
        except ValueError:
            print('only digits')
            
    array.append(num)

print(f"Масив: {array}")
new_array = set(array)

if len(array) != len(new_array):
    print("have the same numbers")
else:
    print("have not the same numbers")
