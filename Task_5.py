"""
Напишите функцию, которая принимает словарь с параметрами
и возвращает строку запроса, сформированную из отсортированных
в лексикографическом порядке параметров.
Пример:
Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17})) должен возвращать строку:
challenge=17&course=python&lesson=2
"""

def query(dict_temp):
    dict_temp = dict(sorted(dict_temp.items()))
    res_string = ''
    for (k, v) in dict_temp.items():
        res_string += f'{k}={v}&'
    res_string = res_string.rstrip(res_string[-1])
    return res_string


dictionary_user = {'course': 'python', 'lesson': 2, 'challenge': 17}


print(query(dictionary_user))

