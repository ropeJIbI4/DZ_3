# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def number_composition(number_list):
    l = len(number_list)//2 + 1 
    if len(number_list) % 2 != 0:
        result = [number_list[i]*number_list[len(number_list)-i-1] for i in range(l)]
    else:len(nuber_list)//2
    result = [number_list[i]*number_list[len(number_list)-i-1] for i in range(l)]
    print(result)

number_dz_one=[2, 3, 4, 5, 6]
number_dz_two=[2, 3, 5, 6]
nuber_list=list(map(int, input("Введите числа через пробел:\n").split()))
number_composition(number_dz_one)
number_composition(number_dz_two)
number_composition(nuber_list)



