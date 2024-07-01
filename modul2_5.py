def get_matrix(m, n, value): # создаём функцию
    matrix = []              # пустой список для функции
    for i in range(n):       # 1 внешний цикл для кол-ва строк n
        matrix.append([])    # добавление списка matrix
        for j in range(m):   # 2 внутренний цикл для кол-ва столбцов m
            matrix[i].append(value) # добавление value для списка matrix внутри 1цикла
    return matrix            # выход из функции

result1 = get_matrix(2, 2, 10) # присвоение значений для 1 результата ф-ции
result2 = get_matrix(3, 5, 42) # присвоение значений для 2 результата ф-ции
result3 = get_matrix(4, 2, 13) # присвоение значений для 3 результата фу-ции
# вывод 3х результатов работы фу-ции в консоль
print(result1)
print(result2)
print(result3)
