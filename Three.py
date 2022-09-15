# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

number_list = [1.1, 1.2, 3.1, 5, 10.01]
number_list_input = list(map(float, input("Введите вещественные числа через пробел:\n").split()))
def number_float(number_list):
    min = 1.0
    max = 0.0
    for i in number_list:
        if (i - int(i)) <= min:
            min = i - int(i)
        if (i - int(i)) >= max:
            max = i - int(i)
    print(max-min)  
number_float(number_list)
number_float(number_list_input)