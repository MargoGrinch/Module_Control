'''
49. Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.
'''

table = ["Apple", "Banana", "Pineapple", "Orange", "Plum", "Mango", "Tangerin", "Blueberry"]
cost = [34, 23, 45, 36, 78, 45, 95, 65]
G = 95# ціна
sel = cost.index(G)
for i in  range(sel):
    print(f"Услуга: {table[i]}, Цена: {cost[i]} грн")
