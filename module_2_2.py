first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first != second and third:
    print(0)
elif first == second and third:
    print(3)
elif first == second or third:
    print(2)