'''
55. У будинку, що складається з 30 квартир, переселити мешканців так, щоб
мешканці першої квартири переїхали в тридцяту, з тридцятого - в першу, з другої - в 29
і т.д., знайдіть кількість квартир, в яких проживає більше 5 осіб.
'''

import numpy as np

flats = np.random.randint(0, 10, 30)
print(f"Flats: {flats}")

count = flats[flats > 5]

flats = flats[::-1]

print(f"Flats after transmition: {flats}")
print(f"More than 5 people: {len(count)}")
