#  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

number_list=[2, 3, 5, 9, 3]
number_list_input = list(map(int, input("Введите числа через пробел:\n").split()))
def summ(number_list):
 """ищет суму на нечетных позициях """
 print(sum(number_list[1::2]))
summ(number_list)
summ(number_list_input)