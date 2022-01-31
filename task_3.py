"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

company = {
    'dex': 100,
    'kio': 200,
    'jou': 50,
    'bad': 500,
    'qyt': 1100
}

# 1
sorted_val = sorted(company.values(), reverse=True)
result = {}
for i in sorted_val:
    for k in company.keys():
        if company[k] == i:
            result[k] = i
            break
print(result)

# 2
sorted_val = sorted(company.items(), key=lambda x: x[1], reverse=True)
result = {key: val for key, val in sorted_val}
print(result)

# 3
sorted_val = sorted(company, key=company.get, reverse=True)
for i in sorted_val:
    result[i] = company[i]
print(result)
