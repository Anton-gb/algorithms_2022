"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

import random

box = []
for i in range(1, 7):
    box.append(random.randint(-100, 100))

print(box, f'min: {min(box)}')

# 1
case = box[0]
for i in box[1:]:       # O(n)
    if i > case:
        box.remove(i)   # O(n)
    elif i < case:
        box.remove(case)
        case = i
print(box)

# 2
case = box[0]
for i in box:           # O(n)
    if i < case:
        case = i
print(case)

