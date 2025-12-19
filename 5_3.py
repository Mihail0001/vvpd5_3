import numpy as np

array = None
rows, cols = 0, 0

def print_functions_menu():
    print("1. Напечатать индексы отрицательных элементов массива")
    print("2. Вывести на экран элементы массива, кратные 5, и их индексы")
    print("3. Найти количество положительных элементов массива, расположенных выше главной диагонали")
    print("4. Поменять местами первый и последний столбец")
    print("5. Вычислить сумму положительных элементов в строках без нулевых элементов")
    print("6. Назад")

def function_1():
    if array is None:
        print("Массив не создан!")
        return
    
    print("Индексы отрицательных элементов:")
    found = False
    for i in range(rows):
        for j in range(cols):
            if array[i][j] < 0:
                print(f"[{i}][{j}] = {array[i][j]}")
                found = True
    if not found:
        print("Отрицательных элементов нет")

def function_2():
    if array is None:
        print("Массив не создан!")
        return
    
    print("Элементы, кратные 5, и их индексы:")
    found = False
    for i in range(rows):
        for j in range(cols):
            if array[i][j] % 5 == 0:
                print(f"[{i}][{j}] = {array[i][j]}")
                found = True
    if not found:
        print("Элементов, кратных 5, нет")