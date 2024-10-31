data_structure = [

    [1, 2, 3],

    {'a': 4, 'b': 5},

    (6, {'cube': 7, 'drum': 8}),

    "Hello",

    ((), [{(2, 'Urban', ('Urban2', 35))}])

]


# Вариант 1 с добавлением в список.

def calculate_structure_sum(lst):
    list_add = []
    for el in lst:
        if isinstance(el, str):
            list_add.append(len(el))
        elif isinstance(el, dict):
            for k, v in el.items():
                list_add.append(len(k))
                list_add.append(v)
        elif isinstance(el, list) or isinstance(el, tuple) or isinstance(el, set):
            list_add.extend(calculate_structure_sum(el))
        else:
            list_add.append(el)
    return list_add


result = calculate_structure_sum(data_structure)
print(result)  # Так выглядит наш список после добавления всех элементов
result = sum(result)  # Суммируем. Можно вывести и так - print(sum(result)), но выведем, как условлено в задании.
print(result)  # 99


# Вариант 2 с суммированием в переменную.

def calculate_structure_sum(lst):
    res = 0
    for el in lst:
        if isinstance(el, str):
            res += len(el)
        elif isinstance(el, dict):
            for k, v in el.items():
                res += len(k)
                res += v
        elif isinstance(el, list) or isinstance(el, tuple) or isinstance(el, set):
            res += calculate_structure_sum(el)
        else:
            res += el
    return res


result = calculate_structure_sum(data_structure)
print(result)  # 99
