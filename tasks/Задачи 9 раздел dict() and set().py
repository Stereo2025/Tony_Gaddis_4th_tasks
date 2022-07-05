# - 1 - Информация об учебных курсах. Напишите программу, которая создает словарь,
#       содержащий номера курсов и номера аудиторий, где проводятся курсы. Словарь должен
#       иметь приведенные в табл. 9 .2 пары ключ/значение.
#   Таблица 9.2
#   Номер курса (ключ)  Номер аудитории (значение)
#           CS101               3004
#           CS102               4501
#           CS103               6755
#           CS104               1244
#           CS105               1411
#
#       Программа должна также создать словарь, содержащий номера курсов и имена преподавателей,
#       которые ведут каждый курс. Словарь должен иметь приведенные в табл. 9.3
#       пары ключ/значение.
#   Таблица 9.3
#   Номер курса (ключ)  Преподаватель (значение)
#           CS101               Хайнс
#           CS102               Альварадо
#           CS103               Рич
#           NТ110               Берк
#           СМ241               Ли

#       Программа должна также создать словарь, содержащий номера курсов и время проведения
#       каждого курса. Словарь должен иметь приведенные в табл. 9.4 пары ключ/значение.
#   Таблица 9.4
#   Номер курса (ключ)  Время (значение)
#           CS101               8:00
#           CS102               9:00
#           CS103               10:00
#           NT110               11:00
#           СМ241               13:00

# Программа должна позволить пользователю ввести номер курса, а затем показать номер
# аудитории, имя преподавателя и время проведения курса.

# Решение:

# dict_1 = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755', 'CS104': '1244', 'CS105': '1411'}
# dict_2 = {'CS101': 'Хайнс', 'CS102': 'Альварадо', 'CS103': 'Рич', 'NT110': 'Берк', 'CM241': 'Ли'}
# dict_3 = {'CS101': '8:00', 'CS102': '9:00', 'CS103': '10:00', 'NT110': '11:00', 'CM241': '13:00'}
# curs = input('Enter curs number: ')
# try:
#     print(f'Номер аудитории: {dict_1[curs]}\n'
#           f'Имя преподавателя: {dict_2[curs]}\n'
#           f'Время начала занятий: {dict_3[curs]}')
# except KeyError:
#     print('Номера аудитории нет, есть только:\n'
#           'Имя преподавателя', dict_2[curs], 'и время начала занятий:', dict_3[curs])

# - 2 - Напишите программу, которая создает словарь, содержащий в качестве ключей названия американских
#       штатов и в качестве значений их столицы.Затем программа должна провести викторину, случайным
#       образом выводя название штата и предлагая ввести его столицу. Программа должна провести подсчет
#       количества правильных и неправильных ответов.

# Решение:

# import random
#
#
# US = {'Колумбия': 'Вашингтон', 'Айдахо': 'Бойсе', 'Айова': 'Де-Мойн'}
# count_1, count_2 = 0, 0
# yes = 'd'
# while yes.lower() == 'd':
#     print('Столица штата', random.choice([k for k in US for x in US[k]]), '?')
#     answer = input('Введите столицу штата: ')
#     if answer in US.values():
#         count_1 += 1
#     else:
#         count_2 += 1
#     yes = input('Продолжаем ? d/n: ')
# print('Викторина окончена, правильных ответов:', count_1, 'неправильных: ', count_2)

# - 3 - Напишите программу, которая применяет словарь для присвоения "кодов" каждой букве алфавита. Например:
#       codes = {'A': '!', 'a': '9', 'B': '@', 'b': '8', 'C': '#', 'c': '7', 'D': '$', 'd': '6', 'E': '%', 'e': '5',
#         'F': '^', 'f': '4', 'G': '*', 'g': '3', 'L': '(', 'l': '2', 'M': ')', 'm': '1', 'N': '~', 'n': '0'......}
#       Программа должна открыть заданный текстовый файл, прочитать его содержимое и применить словарь для записи
#       зашифрованной версии содержимого файла во второй файл.

#       Каждый символ во втором файле должен содержать код для соответствующего символа из первого файла.
#       Напишите вторую программу, которая открывает зашифрованный файл и показывает его дешифрованное содержимое на экране.

# Решение:

# dickt = {'Q': '!', 'q': '9', 'W': '@', 'w': '!', 'E': '#', 'e': '#', 'R': '$', 'r': '$', 'T': '%', 't': '5',
#          'Y': '^', 'y': '4', 'U': '*', 'u': '3', 'I': '(', 'i': '2', 'O': ')', 'o': '-', 'P': '~', 'p': '0',
#          'A': '=', 'a': '1', 'S': '+', 's': '2', 'D': '_', 'd': '3', 'F': '/', 'f': '4', 'G': '|', 'g': '5', 'H': '{',
#          'h': '$', 'J': '}', 'j': '#', 'K': '[', 'k': '!', 'L': ']', 'l': '9', 'Z': '<', 'z': '0', 'X': '>', 'x': '<>',
#          'C': '?', 'c': '-', 'V': ':', 'v': '2', 'B': ';', 'b': '3', 'N': ';', 'n': '@', 'M': '.', 'm': '*',
#          ',': ',', '-': '-', '.': '.', ' ': ' '}
#
# with open('Английский стих.txt') as text:
#     list_1 = [i.strip() for i in text.readlines()]
#
#
# for i in list_1:
#     output = ''.join(dickt[c] for c in i)
#
#     file = open('space.txt', 'a')
#     file.write(str(output) + '\n')
#     file.close()
#
# file_2 = open('Английский стих.txt')
# new_file_2 = file_2.read()
# print(new_file_2)
#
# file_1 = open('space.txt', 'r')
# new_file = file_1.read()
# print(new_file)

# - 4 - Напишите программу, которая открывает заданный текстовый файл и затем показывает список всех уникальных слов
#       в файле.
# Решение:
# 1 - Читать текстовый файл в режиме чтения. read()
# 2 - Преобразовать текст в нижний регистр или верхний регистр.
# 3 - Разделить содержимое файла в список слов. split()
# 4 - Очистить слова, которые заражены знаками препинания .strip()
# 5 - Удалить ApoStrophe-S ‘s Отказ: .replace("'s", '')
# 6 - Создать пустой список
# 7 - переменная = text.split, .strip("''.,!;()[]-") and .word.replace("'s", '')
# 8 - Если переменной word нету в пустом списке:
# 9 - Сортировать слова
# 10 - Сортировка слов в столбик циклом

# text_file = open('Английский стих.txt', 'r')
# text = text_file.read()
#
# text = text.lower()
# words = text.split()
# words = [word.strip("''.,!;()[]-") for word in words]
# words = [word.replace("'s", '') for word in words]
#
# unique = []
# for word in words:
#     if word not in unique:
#         unique.append(word)
# unique.sort()
#
# for stolbik in unique:
#     print(stolbik)
# print(unique)

# - 5 - Напишите программу, которая считывает содержимое текстового файла. Она должна создать словарь, в котором ключами
#       являются отдельные слова в файле, и значениями - количество появлений каждого слова. Например, если слово
#       'это' появляется 128 раз, то словарь должен содержать элемент с ключом 'это' и значением 128. Программа должна
#       либо показать частотность каждого слова, либо создать второй файл, содержащий список слов и их частотностей.
# Решение:
# def read():
#     file = input('Enter a file name with its extension: ')
#     object_file = open(file, 'r')
#     return object_file
#
# def count(object_file):
#     word_frequency = {}
#     count = 1
#     for line in object_file:
#         words = line.split()
#         for word in words:
#             word = word.lower()
#             if word not in word_frequency:
#                 word_frequency[word] = count
#             else:
#                 word_frequency[word] = count + 1
#
#     print(word_frequency)
# object_file = read()
# count(object_file)

# - 6 - Напишите программу, которая читает содержимое двух текстовых файлов и сравнивает их следующим образом:
#   • показывает список всех уникальных слов, содержащихся в обоих файлах;
#   • показывает список слов, входящих в оба файла;
#   • показывает список слов из первого файла, не входящих во второй;
#   • показывает список слов из второго файла, не входящих в первый;
#   • показывает список слов, входящих либо в первый, либо во второй файл, но не входящих в оба файла одновременно.

# Решение:
# 1 - Читать текстовый файл в режиме чтения. read()
# 2 - Преобразовать текст в нижний регистр или верхний регистр.
# 3 - Разделить содержимое файла в список слов. split()
# 4 - Очистить слова, которые заражены знаками препинания .strip()
# 5 - Удалить апостроф ‘s: .replace("'s", '')
# 6 - Создать пустой список
# 7 - переменная = text.split, .strip("''.,!;()[]-") and .word.replace("'s", '')
# 8 - Если переменной word нету в пустом списке:
# 9 - Сортировать слова
# 10 - Сортировка слов в столбик циклом
# 11 - Применить пункты 1 - 10 к следующему файлу
# 12 - Создать пустой список и применить между сетов: intersection
# 13 - Создать пустой список и применить между сетов: union
# 14 - Создать пустой список и применить между сетов: difference
# 15 - Создать пустой список и применить между сетов: symmetric_difference

# def main():
#     text_file = open('Английский стих.txt', 'r')
#     text = text_file.read()
#     text = text.lower()
#     words = text.split()
#     words = [word.strip("''.,!;()[]-") for word in words]
#     words = [word.replace("'s", '') for word in words]
#     unique = []
#     for word in words:
#         if word not in unique:
#             unique.append(word)
#     unique.sort()
#     sset = set(unique)
#     print(sset)
#
#     print('-' * 40)
#
#     text_file_2 = open('Английский стих_2.txt', 'r')
#     text_2 = text_file_2.read()
#     text_2 = text_2.lower()
#     words_2 = text_2.split()
#     words_2 = [word_2.strip("''.,!;()[]-") for word_2 in words_2]
#     words_2 = [word_2.replace("'s", '') for word_2 in words_2]
#     unique_2 = []
#     for word_2 in words_2:
#         if word_2 not in unique_2:
#             unique_2.append(word_2)
#     unique_2.sort()
#     sset_2 = set(unique_2)
#     print(sset_2)
#
#     print('-' * 40)
#
#     l_1 = []
#     for q in sset.intersection(sset_2):
#         l_1.append(q)
#     print(f'Список уникальных слов содержащихся в обоих файлах:\n{l_1}')
#
#     print('-' * 40)
#
#     l_2 = []
#     for e in sset.union(sset_2):
#         l_2.append(e)
#     print(f'Эти слова есть и в 1м и 2м файле:\n{l_2}')
#
#     print('-' * 40)
#
#     l_3 = []
#     for t in sset.difference(sset_2):
#         l_3.append(t)
#     print(f'Эти слова есть в 1м но не во 2м файле:\n{l_3}')
#
#     print('-' * 40)
#
#     l_4 = []
#     for y in sset_2.difference(sset):
#         l_4.append(y)
#     print(f'Эти слова есть во 2м но не в 1м файле:\n{l_4}')
#
#     print('-' * 40)
#
#     l_5 = []
#     for r in sset_2.symmetric_difference(sset):
#         l_5.append(r)
#     print(f'Эти слова есть во одном файле но не в обоих:\n{l_5}')
#
#
# main()

# - 7 - Победители Мировой серии. Среди исходного кода главы 9, а также в подпапке data
# "Решений задач по программированию" соответствующей главы вы найдете файл
# WorldSeriesWiпners.txt. Этот файл содержит хронологический список командпобедителей
# Мировой серии по бейсболу с 1903 по 2009 годы. (Первая строка в файле
# является названием команды, которая победила в 1903 году, последняя строка - названием
# команды, которая победила в 2009 году. Обратите внимание, что Мировая серия не
# проводилась в 1904 и 1994 годах. В файле имеются указывающие на это пометки.)
# Напишите программу, которая читает этот файл и создает словарь, в котором ключиэто
# названия команд, а связанные с ними значения - количество побед команды в Мировой
# серии. Программа должна также создать словарь, в котором ключи - это годы, а связанные
# с ними значения - названия команд, которые побеждали в том году.
# Программа должна предложить пользователю ввести год в диапазоне между 1903 и
# 2009 годами и должна вывести название команды, которая выиграла Мировую серию
# в том году и количество побед команды в Мировой серии.

# Решение:

# file = "WorldSeriesWinners.txt"
#
# def description():
#
#     print('This program makes two dictionaries from a text file, prompt a user'
#           'to enter a year and display a team won World Series in the year and'
#           'the time to win World Series.\n')
#
# def open_file():
#
#     return open(file, 'r')
# def make_dict(file_object):
#     champ_dict = {}
#     line = file_object.readline().rstrip('\n')
#
#     for i in range(1903, 2010):
#         champ_dict[i] = line
#         line = file_object.readline().rstrip('\n')
#     print(champ_dict, '\n')
#     numb_dict = {}
#     for i in range(1903, 2010):
#         team = champ_dict[i]
#         if not team in numb_dict:
#             numb_dict[team] = 1
#         else:
#             numb_dict[team] += 1
#     print(numb_dict, '\n')
#     return champ_dict, numb_dict
#
# def get_prompt(champ_dict, numb_dict):
#
#     valid = True
#     while valid:
#         try:
#             year = int(input('Enter a year in the range from 1903 to 2009 to '
#                              'know which team won World Series in the year: '))
#             if year > 1902 and year < 2010 and year != 1904 and year != 1994:
#                 print(champ_dict[year], 'won in the year!', numb_dict[champ_dict[year]], 'times')
#                 valid = False
#             elif year == 1904:
#                 print('World Series Not Played in 1904')
#                 valid = False
#             elif year == 1994:
#                 print('World Series Not Played in 1994')
#                 valid = False
#         except:
#             print('Enter a year in integer.')
#
# def main():
#     description()
#
#     file_object = open_file()
#     champ_dict, numb_dict = make_dict(file_object)
#
#     get_prompt(champ_dict, numb_dict)
#
# main()

# - 8 - Имена и адреса электронной почты. Напишите программу, которая сохраняет имена и
# адреса электронной почты в словаре в виде пар ключ/значение. Программа должна вывести
# меню, которое позволяет пользователю отыскать адрес электронной почты человека,
# добавить новое имя и адрес электронной почты, изменить существующий адрес электронной
# почты и удалить существующее имя и адрес электронной почты. Программа
# должна законсервировать словарь и сохранить его в файле при выходе пользователя из
# программы. При каждом запуске программы она должна извлечь словарь из файла и его
# расконсервировать.

# Решение:
# - 1 - Этап
# 1 - импорт модуля pickle
# 2 - создать функцию
# 3 - открыть файл для консервации объекта - 'любое имя.dat', 'wb'
# 4 - вернуть переменную из пункта 3
# import pickle


# def open_file():
#     output_file = open('mailing_list.dat', 'wb')
#     return output_file


# - 2 - Этап
# 5 - создать функцию
# 6 - создать пустой словарь на основе имени файла
# 7 - назначать итератор для цикла while
# 8 - создать цикл while
# 9 - спросить имя, спросить адрес почты
# 10 - добавить в словарь ключ- значение "имя - адрес"
# 11 - спросить о продолжении
# 12 - вернуть словарь
# def make_mailing_list():
#     mailing_list = {}
#     validation = 'y'
#     while validation == 'y':
#         name = input('Введите имя: ').lower()
#         email = input('Введите адрес электронной почты: ').lower()
#         mailing_list[name] = email
#         validation = input('Введите "Y" или "y" для продолжения: ').lower()
#     return mailing_list

# - 3 - Этап
# 13 - создать функцию, задать аргумент в виде словаря
# 14 - задать итератор цикла while
# 15 - написать цикл while
# 16 - создать меню с вопросами для пользователя "Look up, Add, Change или Delete" и "ничего не делать"
# 17 - создать комплекс условных операторов if, elif, с вызовом соответствующих функций
#      последний должен быть == n
# def menu(mailing_list):
#     validation = 'y'
#     while validation == 'y':
#         select_menu = input('Что мы будем делать?\nВведите "Look up", "Add",'
#                             '"Change" или "Delete":\n'
#                             'Если ничего не делать введите "N" или "n": ').lower()
#         if select_menu == 'look up':
#             mailing_list = look_up(mailing_list)
#
#         elif select_menu == 'add':
#             mailing_list = add(mailing_list)
#
#         elif select_menu == 'change':
#             mailing_list = change(mailing_list)
#
#         elif select_menu == 'delete':
#             mailing_list = delete(mailing_list)
#
#         elif select_menu == 'n':
#             print('Увидимся!')
#             validation = 'n'

# - 4 - Этап
# 18 - создать функцию просмотра
# 19 - спросить имя
# 20 - вывести на принт аргумент\словарь с ключом " ключ - имя "
# 21 - вернуть аргумент\словарь
# def look_up(mailing_list):
#     name = input('Введите имя: ').lower()
#     print(mailing_list[name])
#     return mailing_list

# - 5 - Этап
# 22 - создать функцию добавления
# 23 - спросить имя и емэил
# 24 - добавить в словарь ключь - значение " имя - адрес"
# 25 - ввернуть словарь
# def add(mailing_list):
#     name = input('Введите имя: ').lower()
#     email = input('Введите адрес электронной почты: ').lower()
#     mailing_list[name] = email
#     return mailing_list

# - 6 - Этап
# 26 - создать функцию изменения
#    - запросить имя
# 27 - вывести на принт текущий словарь " ключ "
# 28 - запросить подтверждение изменения
# 29 - если да, запросить новый емэил
# 30 - записать его в словарь
# 31 - вернуть словарь
# def change(mailing_list):
#     name = input('Введите имя: ').lower()
#     print(mailing_list[name])
#     validation = input('Введите "Y" или "y" для изменения: ').lower()
#     if validation == 'y':
#         email = input('Введите адрес электронной почты: ').lower()
#         mailing_list[name] = email
#     return mailing_list

# - 7 - Этап
# 32 - создать функцию удаления
# 33 - запросить имя
# 34 - вывести на принт текущий словарь "ключ"
# 35 - запросить подтверждение изменения
# 36 - если да, удалить введенное имя
# 37 - вернуть словарь
# def delete(mailing_list):
#     name = input('Введите имя: ').lower()
#     print(mailing_list[name])
#     validation = input('Введите "Y" или "y" для удаления: ').lower()
#     if validation == 'y':
#         del mailing_list[name]
#     return mailing_list

# - 8 - Этап
# 38 - output_file = open_file()                - имя файла == имени функции
# 39 - mailing_list = make_mailing_list()       - имя словаря "=" имени функции
# 40 - menu(mailing_list)                       - меню
# 41 - pickle.dump(mailing_list, output_file)   - модуль для расконсервации "имя словаря, имя файла"
# 42 - output_file.close()                      - закрыть файл
# output_file = open_file()
# mailing_list = make_mailing_list()
# menu(mailing_list)
# pickle.dump(mailing_list, output_file)
# output_file.close()
