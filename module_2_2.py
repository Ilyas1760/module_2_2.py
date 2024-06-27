first = input('Введите число: ')
second = input('ВВведите число: ')
third = input('Введите число: ')
if first == second == third:
    print(3)
elif first == second or first == third:
    print(2)
elif second == first or second == third:
    print(2)
else:
    print(0)