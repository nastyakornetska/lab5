'''N = int(input("Введіть кількість членів послідовності N: "))
suma = 0
for i in range(1, N + 1):
    drib = (2 * i + 1) / (i + 1)
    suma += drib
print(f"Сума перших {N} членів послідовності дорівнює: {suma}")'''


'''
N = int(input("Введіть значення N: "))  # Кількість членів послідовності
K = int(input("Введіть значення K: "))  # Задане число
sum_of_A = 0
count = 0
for current_number in range(K + 1, K + N + 1):
    if current_number > K: 
        sum_of_A += current_number  
        count += 1  
        if count >= N:  
            break
print("Сума перших", N, "членів послідовності, які більші за", K, ":", sum_of_A)
'''



'''
N = int(input("Введіть розмір матриці N (2 <= N < 99): "))

if 2 <= N < 99:
    matrix = [[0 for _ in range(N)] for _ in range(N)]  
    
    for i in range(N):
        for j in range(N):
            if i == j:
                matrix[i][j] = 0
            elif i > j:
                matrix[i][j] = i * 10 + j
            else:
                matrix[i][j] = j * 10 + i

    for row in matrix:
        print(*row)

else:
    print("Некоректне значення N. Введіть число від 2 до 99.")

'''


import math

a = float(input("Введіть початок відрізка a: "))
b = float(input("Введіть кінець відрізка b: "))
h = float(input("Введіть крок h: "))

if b <= a:
    print("Кінець відрізка має бути більшим за початок.")
elif h <= 0:
    print("Крок має бути додатним числом.")
else:
    x = a
    while x <= b:
        try:
            y = 1 / math.sqrt(9 - x**2) + math.log(2 - x)
            print(f"x = {x:.2f}, y = {y}")
        except ValueError:
            print(f"x = {x:.2f}, Помилка: Значення x виходить за межі області визначення функції")
        x += h

