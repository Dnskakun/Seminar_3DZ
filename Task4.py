"""
Напишите программу, которая принимает на вход две строки
и определяет, являются ли они анаграммами. Знаки препинания,
пробелы и регистр при этом игнорируются.

Пример ввода:
Цари, вино и сало.
Лисица и ворона.

Пример вывода:
YES
"""

import string

def comparison_string(str_1, str_2):
    #str_1 = re.sub(r'[^\w\s]','', str_1)
    str_1 = ''.join((filter(str.isalnum, str_1))).lower()
    str_2 = ''.join((filter(str.isalnum, str_2))).lower()
    if len(str_1) == len(str_2):
        list_1 = sorted(list(str_1))
        list_2 = sorted(list(str_2))
        if list_1 == list_2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
    
    


print("Сейчас мы проверим являются ли строки анаграммами.")
string_1 = input("Введите первую строку: ")
string_2 = input("Введите вторую строку: ")

comparison_string(string_1, string_2)



