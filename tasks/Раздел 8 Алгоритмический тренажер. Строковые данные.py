# - 1 - Допустим, что переменная choice ссылается на строковое значение. Приведенная ниже инструкция if
#       определяет, равна ли переменная choice значениям 'д' или 'д': if choice == 'д' or choice == 'д':
#       Перепишите эту инструкцию так, чтобы она делала всего одно сравнение и использовала  оператор or.
#       (Подсказка: примените метод upper () либо метод lower () .)
# Решение:
# choise = 'д'
# if choise.lower() == 'д' or choise.upper() == 'Д':
#     print(choise)

# - 2 - Напишите цикл, который подсчитывает количество пробельных символов в строковом
#       значении, на которое ссылается mystring.
# Решение:
# mystring = '1 2 3 4 5 '
# c = 0
# for i in mystring:
#     if i == ' ':
#         c += 1
# print(c)

# - 3 - Напишите цикл, который подсчитывает количество цифр в строковом значении, на которое ссылается mystring.
# Решение:
# mystring = '1 2 3 4 5 '
# c = 0
# for i in mystring:
#     if i != ' ':
#         c += 1
# print(c)

# ---------------------------------------------------------------------------------------------------------------------------#
# - 4 - Напишите цикл, который подсчитывает количество символов в нижнем регистре в строковом
#       значении, на которое ссылается mystring.
# Решение:
# s, k = input(), 0
# for i in range(len(s)):
#     if s[i].islower():
#         k+=1
# print(k)

# Решение:
# mystring = 'А б в г д Е'
# count = 0
# for i in mystring:
#     if i.islower():
#         count += 1
# print(count)

# mystring = input(': ')
# d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
# for c in mystring:
#     if c.islower():
#         d['LOWER_CASE'] += 1
#     elif c.isupper():
#         d['UPPER_CASE'] += 1
# print(d)

# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])
# string_test('The quick Brown Fox')
# ---------------------------------------------------------------------------------------------------------------------------#

# - 5 - Напишите функцию, которая принимает строковое значение в качестве аргумента и возвращает
#       истину, если аргумент заканчивается подстрокой ' .com'. В противном случае функция должна вернуть ложь.
# Решение:
# filename = input('Введите имя файла: ')
# if filename.endswith('.com'):
#     print('Этo имя текстового файла.')
# else:
#     print('Такой файл не найден')

# - 6 - Напишите фрагмент кода, делающий копию строкового значения, в котором все вхождения
#       буквы 'т' в нижнем регистре преобразованы в верхний регистр.
# Решение:
# letters = 'Соответствует'
# letters_1 = letters.replace('т', 'Т')
# print(letters_1)

# - 7 - Напишите функцию, которая принимает строковое значение в качестве аргумента и показывает
#       строковое значение в обратном порядке.
# Решение:
# name = 'Hello World !'
# print(name[::-1])

# - 8 - Допустим, что переменная mystring ссылается на строковое значение. Напишите инструкцию,
#       которая применяет выражение среза и показывает первые 3 символа в строковом значении.
# Решение:
# mystring = 'Kak dela'
# print(mystring[:4])

# - 9 - Допустим, что переменная mystring ссылается на строковое значение. Напишите инструкцию,
#       которая применяет выражение среза и показывает последние 3 символа в строковом значении.
# Решение:
# mystring = 'Kak dela'
# print(mystring[-3:])

# - 1О - Взгляните на приведенную ниже инструкцию: mystring = 'пирожки>молоко>стряпня>яблочный пирог>мороженое'
#        Напишите инструкцию, которая разбивает это строковое значение, создавая приведенный ниже список:
#        ['пирожки', 'молоко', 'стряпня', 'яблочный: пирог', 'мороженое']
# Решение:
# mystring = 'пирожки>молоко>стряпня>яблочный пирог>мороженое'
# l = mystring.replace('>', ' ')
# print(l.split())









































