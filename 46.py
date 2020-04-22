'''
46. Задана таблиця назв товарів, що випускаються заводом. Визначте, чи
повторюється в цій таблиці назва першого товару, і, якщо повторюється, видаліть
назву першого товару з таблиці.
'''
table = ["Apple", "Banana", "Pineapple", "Orange", "Plum", "Mango", "Tangerin", "Blueberry"]
if table[0] in table[1:]:
    del table[0]
print(table)
