'''
57. Відомість на зарплату представлена як дві таблиці. Одна містить
прізвища працівників цеху, а друга - їх зарплату за поточний місяць. Знайдіть прізвище
працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою
заробітною платою. Видаліть з відомості на зарплату відомості про працівника,
зарплата якого мінімальна.
'''

import numpy as np
import math

table = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson"]
salary = [34, 23, 15, 34, 23, 65, 12, 75]

rez = np.array(table)
s1 = np.array(salary)
s2 = np.array(salary)
average = np.average(s1)
m = 0
cout = 0

for i in range(len(salary)):
    if math.fabs(average - salary[i]) < m:
        m = math.fabs(average - salary[i])
        cout = i

print(f"Surname worker that have the smallest salary from average: {table[cout]}")

first = (np.where(s2 == s2.max()))[0][0]
s2[first] = s2.min()
second = (np.where(s2 == s2.max()))[0][0]

print(f"Surname of two workers that have the bigest salary: {table[first], table[second]}")

last = (np.where(s1 == s1.min()))[0][0]
s1 = np.delete(s1, last)
rez = np.delete(rez, last)

print(rez)
print(s1)
