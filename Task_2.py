"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка
содержит число X.
5
1 2 3 4 5
6
"""
from random import randint

def user_input(message, min_elem, max_elem):
    input_error: bool = True
    while input_error:
        try:
            number = int(input(message))
        except:
            print("Вы ввели не число!")
        else:
            if min_elem <= number <= max_elem:
                input_error = False
            else:
                print("Вы ввели число, не соответствующее условию!")
    return number

def check_number(temp_list, num):
    temp_diff = abs(list_1[0] - num)
    for i in range(len(temp_list)):
        difference = abs(temp_list[i] - num)
        if difference < temp_diff:
            temp_diff = difference
            temp_index = i

    return temp_index


quantity_elements = user_input(message = "Введите кол-во элементов массива (от 1 до 1000): ", min_elem = 1, max_elem = 1000)
list_1 = [randint(1, 1000) for i in range(quantity_elements)]
number = user_input(message = "Введите какой элемент проверить (от 1 до 1000): ", min_elem = 1, max_elem = 1000)

print(list_1)
print(f'Самый близкий элемент к заданному числу: {list_1[check_number(list_1, number)]}.')



