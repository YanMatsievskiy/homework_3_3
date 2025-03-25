'''Задача 3. Star stair'''

# Решение 1
h = int(input('Введите целое положительное число - высоту лестницы: '))

for i in range(1, h + 1):
    for j in range(1, i + 1):
        print('*', end='')
    print()

# Решение 2
h = int(input('Введите целое положительное число - высоту лестницы: '))

for i in range(1, h + 1):
    print('*' * i)