# - 1 - Напишите функцию с именем times_ten. Эта функция должна принимать аргумент и показывать
#       результат произведения аргумента на 1О.

# Решение:
# def times_ten(num):
#     print(num * 10)
# times_ten(5)

# - 2 - Исследуйте приведенный ниже заголовок функции, затем напишите инструкцию, которая
#       вызывает эту функцию, передавая 12 в качестве аргумента. def show_value(quantity):

# Решение:
# def show_value(quantity):
#     print(quantity)
# show_value(12)

# - 3 - Взгляните на приведенный заголовок функции: def my_function(a, Ь, с):
#       Теперь взгляните на приведенный вызов функции my_function: my_function(3, 2, 1)
#       Какое значение будет присвоено а, когда этот вызов исполнится? Какое значение будет
#       присвоено b? Какое значение будет присвоено с?

# Решение:
# def my_function(a, b, c):
#    print(a, b, c)
# my_function(3, 2, 1)

# - 4 - Что покажет приведенная ниже программа?
# def main ():
#     x = 1
#     y = 3.4
#     print (x, y)
#     change_us(x, y)
#     print (x, y)

# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)
# main ()

# Решение: 1, 3.4, 0,0 , 1, 3.4

# - 5 - Взгляните на приведенное ниже определение функции my_func:
# def my_function(a, Ь, с):
#     d = (а + с) / Ь
#     print (d)
#  • Напишите инструкцию, которая вызывает эту функцию и применяет именованные аргументы для передачи
#    2 в а, 4 в b и 6 в с.
#  • Какое значение будет показано, когда исполнится вызов функции?

# Решение:
# def my_function(a, b, с):
#     d = (a + с) / b
#     print (d)
# my_function(2, 4, 6)

# - 6 - Напишите инструкцию, которая генерирует случайное число в диапазоне от 1 до 100
#       и присваивает его переменной с именем rand.

# Решение:
# import random
# rand = random.randint(1, 100)
# print(rand)

# - 7 - Приведенная ниже инструкция вызывает функцию half, возвращающую значение, которое вдвое меньше аргумента.
#       (Допустим, что переменная number ссылается на вещественное значение с типом float.)
#       Напишите код для этой функции. result = half(number)

# Решение: - непонятно....
# def half():
#    number = 5.5
#    print(number)
# half()

# - 8 - Программа содержит приведенное ниже определение функции:
# def cube (num) :
#     return num * num * num
#   Напишите инструкцию, которая передает значение 4 в эту функцию и присваивает возвращаемое ею значение
#   переменной result.

# Решение:

# def cube(num):
#     return num * num * num
# print(cube(4))

# - 9 - Напишите функцию times_ten, которая принимает number в качестве аргумента. Когда
#       функция вызывается, она должна возвращать значение ее аргумента, умноженное на 1О.

# Решение:
# def times_ten(number):
#    return number
# print(times_ten(5 * 10))

# - 10 - Напишите функцию get_first_name, которая просит пользователя ввести свое имя и его возвращает.

# Решение:
# def get_first_name():
#    username = input('Press your name: ')
#    return username
# print('Hello', get_first_name())
