'''
47. У лінійному масиві знайти максимальний елемент. Вставте порядковий
номер елемента за ним, пересунувши всі залишилися на одну позицію вправо.
'''
a = [14, 22, 38, 45, 142, 221, 313, 32, 712, 310, 9, 7]
i = a.index(max(a))
a.insert(i + 1, i)
print(a)
