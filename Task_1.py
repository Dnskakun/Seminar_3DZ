"""
Задача 16: Требуется вычислить, сколько раз встречается
некоторое число X в массиве A[1..N]. Пользователь в первой
строке вводит натуральное число N – количество элементов
в массиве. В последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X.
Например:
5
1 2 3 4 5
3 -> 1
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
    index = 0
    for i in list_1:
        if num == i:
            index += 1
    return index




quantity_elements = user_input(message = "Введите кол-во элементов массива (от 1 до 1000): ", min_elem = 1, max_elem = 1000)
list_1 = [randint(1, 10) for i in range(quantity_elements)]
number = user_input(message = "Введите какой элемент проверить (от 1 до 1000): ", min_elem = 1, max_elem = 1000)

print(list_1)
print(f'Число {number} встречается в массиве {check_number(list_1, number)} раз.')





