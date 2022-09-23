# Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четверти от 1 - 4: ')
quarter = int(input())

if quarter == 1:
    print('x + and у +')
if quarter == 2:
    print('x - and y +')
if quarter == 3:
    print('x - and y - ')
if quarter == 4:
    print('x + and y -')
else:
    print('Введено некорректное значение')
    
