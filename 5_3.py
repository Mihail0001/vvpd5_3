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

def function_3():
    if array is None:
        print("Массив не создан!")
        return
    
    if rows != cols:
        print("Массив не квадратный! Главная диагональ определена только для квадратных матриц")
        return
    
    count = 0
    for i in range(rows):
        for j in range(cols):
            if j > i and array[i][j] > 0:
                count += 1
    print(f"Количество положительных элементов выше главной диагонали: {count}")

def function_4():
    if array is None:
        print("Массив не создан!")
        return
    
    if cols < 2:
        print("Нужно минимум 2 столбца для замены!")
        return
    
    print("Массив до замены:")
    print(array)
    
    temp = array[:, 0].copy()
    array[:, 0] = array[:, -1]
    array[:, -1] = temp
    
    print("\nМассив после замены первого и последнего столбцов:")
    print(array)