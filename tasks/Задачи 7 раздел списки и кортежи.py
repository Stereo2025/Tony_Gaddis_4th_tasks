# - 1 - Общий объем продаж. Разработайте программу, которая просит пользователя ввести продажи магазина за
#       каждый день недели. Суммы должны быть сохранены в списке. Примените цикл, чтобы вычислить общий объем
#       продаж за неделю и показать результат.

# Решение:
# 1 - создать функцию
# 2 - создать пустой лист
# 3 - создать аккумулятор
# 4 - создать цикл за каждый день недели
# 5 - ввести данные за каждый день недели
# 6 - занести сумму в аккумулятор
# 7 - добавить в лист продажи
# 8 - вывести на принт суммы
# 9 - вывести на принт придажи за каждый день
# 10 - вызвать функцию

# def func(list_, akk):
#     for i in range(1, 8):
#         num = int(input(f'Введите продажи за {i} день: '))
#         list_.append(num)
#         akk += num
#     return f'Суммы сохраненные в листе: {list_}\n' \
#            f'Общий объем продаж: {akk}$'
#
#
# print(func(list_=[], akk=0))

# - 2 - Генератор лотерейных чисел. Разработайте программу, которая генерирует семизначную комбинацию лотерейных чисел.
#       Программа должна сгенерировать семь случайных чисел, каждое в диапазоне от О до 9, и присвоить каждое число
#       элементу списка. (Случайные числа рассматривались в главе 5.) Затем напишите еще один цикл, который показывает
#       содержимое списка.

# Решение:
# 1 - импортировать модуль случайного числа
# 2 - создать функцию
# 3 - создать пустой лист
# 4 - создать цикл в диапазоне до 7
# 5 - добавить в пустой лист рандомные числа от 0 до 9
# 6 - вывести на принт
# 7 - вызвать мэйн

# import random
#
#
# def func(list_):
#     for i in range(1, 8):
#         list_.append(random.randint(0, 9))
#     return list_
#
#
# print(func(list_=[]))

# - 3 - Статистика дождевых осадков. Разработайте программу, которая позволяет пользователю занести в список общее
#       количество дождевых осадков за каждый из 12 месяцев. Программа должна вычислить и показать суммарное количество
#       дождевых осадков за год, среднее ежемесячное количество дождевых осадков и месяцы с самым высоким и
#       самым низким количеством дождевых осадков.

# Решение:
# 1 - создать функцию, объявить аргумент пустым списком
# 2 - сделать цикл за 12 месяцев
# 3 - ввести кол-во осадков за каждый месяц
# 4 - добавить данные в список
# 5 - вывести значения согласно требованию задачи

# def func(list_):
#     for i in range(1, 13):
#         precipitation = int(input(f'Введите кол-во осадков за {i} месяц: '))
#         list_.append(precipitation)
#     return f'Суммарное кол-во осадков за год: {sum(list_)}\n' \
#            f'Среднее ежемесячное количество дождевых осадков: {sum(list_) // len(list_)}\n' \
#            f'Месяц с самым высоким количеством дождевых осадков: {max(list_)}\n' \
#            f'Месяц с самым низким количеством дождевых осадков: {min(list_)}'
#
#
# print(func(list_=[]))

# - 4 - Проrрамма анализа чисел. Разработайте программу, которая просит пользователя ввести ряд из 20 чисел.
#       Программа должна сохранить числа в списке и затем показать приведенные ниже данные:
#   • наименьшее число в списке;
#   • наибольшее число в списке;
#   • сумму чисел в списке;
#   • среднее арифметическое значение чисел в списке.

# Решение:

# def funk(list_):
#     return f'Наименьшее число в списке: {min(list_)}\n' \
#            f'Наибольшее число в списке: {max(list_)}\n' \
#            f'Сумму чисел в списке: {sum(list_)}\n' \
#            f'Среднее арифметическое значение чисел в списке: {sum(list_) // len(list_)}'
#
#
# print(funk(list_=list(map(int, input(': ').split()))))

# - 5 - Проверка допустимости номера расходноrо счета. Среди исходного кода главы 7, а также в подпапке data
#       "Решений задач по программированию" соответствующей главы вы найдете файл charge_accounts.txt.
#       Этот файл содержит список допустимых номеров расходных счетов компании. Каждый номер счета представляет
#       собой семизначное число, в частности 5658845.
#       Напишите программу, которая считывает содержимое файла в список. Затем эта программа должна попросить
#       пользователя ввести номер расходного счета. Программа должна определить, что номер является допустимым,
#       путем его поиска в списке. Если число в списке имеется, то программа должна вывести сообщение, указывающее
#       на то, что номер допустимый. Если числа в списке нет, то программа должна вывести сообщение,
#       указывающее на то, что номер недопустимый.

# Решение:
# 1 - Создать ф-ю, передать аргумент в виде запроса на ввод счета
# 2 - Открыть файл для чтения
# 3 - создать пустой список, поместить в него цикл for в int и чтение readlines()
# 4 - если номер в списке вернуть то, если нет вернуть это. )
# 5 - в принте объявляем ф-ю и запрос на ввод

# def func(addres):
#     with open('charge_accounts.txt') as text:
#         list_ = [int(i) for i in text.readlines()]
#     if addres in list_:
#         return 'Номер допустим'
#     return 'Номер не допустим'
#
#
# print(func(addres=int(input('Ведите номер: '))))

# - 6 - Больше числа n. В программе напишите функцию, которая принимает два аргумента: список и число n.
#       Допустим, что список содержит числа. Функция должна показать все числа в списке, которые больше n.

# Решение:
# 1 - создать функцию
# 2 - задать аргументы функции, список и число n
# 3 - создать список с числами передать в качестве параметра в функцию
# 4 - задать значение n передать в функцию
# 5 - создать два пустых списка
# 6 - создать цикл и пройтись по списку
# 7 - опеределить числа которые больше n и вывести в отдельный список
# 8 - определить числа которые меньше n и вывести в отдельный список

# Решение 1:
# def func(list_1, list_2, n, list_):
#     for i in list_:
#         if i > n:
#             list_1.append(i)
#         elif i < n:
#             list_2.append(i)
#     return f'Больше n: {list_1}\nМеньше n: {list_2}'
#
#
# print(func(list_1=[], list_2=[], n=int(input(': ')), list_=[1, 2, 3, 4, 5, 6, 7]))

# Решение 2 через файл:
# with open('number_list.txt') as text:
#     list_1 = [int(i) for i in text.readlines()]
# l_1 = []
# l_2 = []
# i = 50
# for i in list_1:
#     if i < list_1[50] and i % 2 == 0:
#         l_1.append(i)
#     elif i > list_1[50] and i % 2 == 1:
#         l_2.append(i)
#
# print(f'{l_1}\n{l_2}')

# - 7 - Экзамен на получение водительских прав. Местный отдел по выдаче удостоверений на право вождения автомобиля
#       попросил вас создать приложение, которое оценивает письменную часть экзамена на получение водительских прав.
#       Экзамен состоит из 20 вопросов с множественным выбором. Вот правильные ответы:
#       1.А ;  2.C ;  3.A ; 4.A ;  5.D ;  6.B ;  7.C ;  8.A;  9.C;  10.B;
#       11.А;  12.D;  13.C;  14.A;  15.D;  16.С;  17.B;  18.B;  19.D;  20.А
#       Программа должна прочитать из текстового файла ответы испытуемого на каждый из 20 вопросов и сохранить
#       эти ответы в еще одном списке. После того как ответы испытуемого были считаны из файла, программа должна
#       вывести сообщение о том, прошел ли испытуемый экзамен или нет.
#       (Для того чтобы сдать экзамен, испытуемый должен правильно ответить на 15 из 20 вопросов.)
#       1 - Затем программа должна вывести общее количество вопросов, ответы на которые были
#       правильными.
#       2 - Общее количество вопросов, ответы на которые были неправильными.
#       3 - Список, показывающий номера вопросов, ответы на которые были неправильными.

# Решение 1:
# 1 - создать ф-ю, перечислить аргументы - счетчик правильных неправильных и пустой список с неправильными
# 2 - открыть файл для чтения, прочитать его сразу в список с правильными ответами
# 3 - создать list comprehension через input с ответами студента и циклом в диапазоне длинны списка + 1
# 4 - цикл for в диапазоне длины списка с правильными ответами
# 5 - если ответы пользователя == правильным ответам из списка то:
# 6 - + 1 к правильным
# 7 - если нет то:
# 8 - + 1 к неправильным и добавить в список не правильных номеров неправильного ответа " +1 "
# 9 - вывести на принт все данные

# Решение 1:

# def func(student_solution, correct, wrong, wrong_answers):
#     with open(student_solution) as text:
#         right_answers = [i.strip() for i in text.readlines()]
#         user_answers = [input(f'Введите ответ на {i} вопрос: ').upper()
#                         for i in range(1, len(right_answers) + 1)]
#
#         for i in range(len(right_answers)):
#             if user_answers[i] == right_answers[i]:
#                 correct += 1
#             else:
#                 wrong_answers.append(i + 1)
#                 wrong += 1
#
#         print(f'Правильные ответы: {correct}\n'
#               f'Неправильные ответы: {wrong}\n'
#               f'Список с номерами неправильных ответов: {wrong_answers}\n'
#               f'Список с правильные ответы: {right_answers}\n'
#               f'Список с ответами пользователя: {user_answers}')
#
#
# func('student_solution..txt', correct=0, wrong=0, wrong_answers=[])

# Решение 2 через zip:

# def main(student_solution, correct, wrong, wrong_answers):
#     with open(student_solution) as text:
#         right_answers = [i.strip() for i in text.readlines()]
#         user_answers = [input(f'Введите ответ на {i} вопрос: ').upper()
#                         for i in range(1, len(right_answers)+1)]
#
#         for i in zip(right_answers, user_answers):
#             if len(set(i)) == 1:
#                 correct += 1
#             else:
#                 wrong_answers.append(i[-1])
#                 wrong += 1
#
#         print(f'Правильные ответы {correct}\n'
#               f'Неправильные ответы {wrong}\n'
#               f'Список с неправильными ответами {wrong_answers}\n'
#               f'Список с правильными ответами: {right_answers}\n'
#               f'Список с ответами пользователя: {user_answers}\n')
#
#
# main('student_solution..txt', correct=0, wrong=0, wrong_answers=[])

# - 8 - Поиск имени.
#       Напишите программу, которая считывает содержимое этих двух файлов в два отдельных списка. Пользователь должен
#       иметь возможность ввести имя мальчика, имя девочки или оба имени, и приложение должно вывести сообщения о том,
#       что введенные имена находятся среди самых популярных имен.
# Решение:

# 1 - Открыть 2 файла, с именами девочек и с именами мальчиков, разбить через strip() и цикл, а затем прочитать
#     через readlines()
# 2 - задать пользователю вопрос желает ли он ввести сразу 2 имени, или же найти только девочку или мальчика
# 3 - если да, то: инпут на девокчку и мальчика ну и через принт с условием вывести имееются ли данные имена
#     в списках
# 4 - если нет, то: задать через инпут вопрос кого ищем мальчика или девочку
# 5 - ну и далее если ищем мальчика, если девочка ищем девочку "так же через принт и if"

# def main():
#     with open('GirlNames.txt') as text:
#         file_1 = [i.strip() for i in text.readlines()]
#     with open('BoyNames.txt') as text:
#         file_2 = [i.strip() for i in text.readlines()]
#
#     yes = input('Желаете ввести имя девочки и имя мальчика ?\nY если да: ').lower()
#     if yes == 'y':
#         boy_name = input('Enter boy name: ')
#         girl_name = input('Enter girl name: ')
#         print(f'Имя {boy_name} в списке популярных' if boy_name in file_2 else f'Имя {boy_name} не популярно')
#         print(f'Имя {girl_name} в списке популярных' if girl_name in file_1 else f'Nety {girl_name} не популярно')
#
#     if yes != 'y':
#         ans = input('Ввести имя мальчика или девочки ? ')
#         if ans == 'Boy':
#             boy_name = input('Enter boy name: ')
#             print(f'Имя {boy_name} в списке популярных' if boy_name in file_2 else f'Имя {boy_name} не популярно')
#         if ans == 'Girl':
#             girl_name = input('Enter girl name: ')
#             print(f'Имя {girl_name} в списке популярных' if girl_name in file_1 else f'Nety {girl_name} не популярно')
#
#
# main()


# - 9 - Данные о населении. Файл USPopulation.txt. Этот файл содержит данные о среднегодовой численности
#       населения США в тысячах с 1950 по 1990 годы. Первая строка в файле содержит численность населения в 1950 году,
#       вторая строка - численность населения в 1951 году и т. д.
#       Напишите программу, которая считывает содержимое файла в список. Программа должна показать приведенные ниже
#       данные:
#   • среднегодовое изменение численности населения в течение указанного периода времени;
#   • год с наибольшим увеличением численности населения в течение указанного периода времени;
#   • год с наименьшим увеличением численности населения в течение указанного периода времени.

# Решение:
# создать функцию, определить аргументы
# открыть файл в список в файл переведя в int
# написать цикл по длине списка "1, len(...)"
# создать переменную и записать в неё вычисление чисел из списка "последующее из предыдущего"
# добавить в пустой лист переменную из пункта выше
# написать цикл по листу, добавить в аккумулятор int(переменная цикла)
# ---> промежуточные действия: сортировать список, выяснить мин и макс
# записать в list.index() максимальное значение и минимальное
# записать индекс максимального и минимального числа из несортированного списка

# def func(USPopulation, YEAR, akkum, list_):
#     with open(USPopulation) as text:
#         lst = [int(i) for i in text]
#
#     for elem in range(1, len(lst)):
#         count = lst[elem] - lst[elem - 1]
#         list_.append(count)
#     for i in list_:
#         akkum += int(i)
#
#     print(f'Год с наибольшим приростом: {list_.index(3185) + YEAR} сумма прироста {list_[4]}\n'
#           f'Год с наименьшим приростом: {list_.index(1881) + YEAR} сумма прироста {list_[16]}\n'
#           f'Среднегодовое изменение: {akkum // len(list_)}')
#
#
# func('USPopulation.txt', YEAR=1950, akkum=0, list_=[])
#############
# YEAR = 1950
# def main():
#     spisok = []
#     file = open('USPopulation.txt')  # открывает файл txt
#     list = [int(e.rstrip()) for e in file]  # преобразует строковые значения "числа" в int и записывает в список
#     total = 0
#     for elem in range(1, len(list)):
#         x = list[elem] - list[elem - 1]
#         spisok.append(x)
#     for i in spisok:
#         total += int(i)
#     print(f'Год с наивысшим приростом: {spisok.index(3185) + YEAR} сумма прироста {spisok[4]}\n'
#           f'Год с наименьшим приростом: {spisok.index(1881) + YEAR} сумма прироста {spisok[16]}\n'
#           f'Среднегодовое изменение численности: {total // len(spisok)}')
# main()

# - 10 - Среди исходного кода главы 7, а также в подпапке data "Решений задач по программированию" соответствующей
#   главы вы найдете файл WorldSeriesWinners.txt. Этот файл содержит хронологический список команд-победителей
#   Мировой серии по бейсболу с 1903 по 2009 годы. (Первая строка в файле является названием команды, которая победила
#   в 1903 году, а последняя строка является названием команды, которая победила в 2009 году. Обратите внимание,
#   что Мировая серия не проводилась в 1904 и 1994 годах.)
#   Напишите программу, которая позволяет пользователю ввести название команды и затем выводит количество лет,
#   когда команда побеждала в Мировой серии в течение указанного периода времени с 1903 по 2009 годы.
# Решение 1:

# 1- Создать ф-ю, задать аргумент файлом и инпутом имени команды
# 2- открыть файл в список
# 3- в принте посчитать через count(name) сколько раз встречается тима.

# def func(WorldSeriesWinners, name_team):
#     with open(WorldSeriesWinners)as text:
#         list_ = [i.strip() for i in text]
#
#     print(f'Команда {name_team} побеждала: {list_.count(name_team)} раз'
#           if name_team in list_ else 'Такой команды нет')
#
#
# func('WorldSeriesWinners.txt', input(': '))

# Решение 2 через дикт:
# def main(WorldSeriesWinners, name_team):
#     with open(WorldSeriesWinners) as text:
#         file = [i.strip() for i in text]
#
#     # динамическое создание словаря: ключ - нэйм тимы, значение - кол-во побед.
#     d = {i: file.count(i) for i in file}
#     print('За указанный период данная команда побеждала', d[name_team], 'раз')
#
#
# main('WorldSeriesWinners.txt', input('Введите команду: '))


# - 11 - Магический квадрат Ло Шу. Магический квадрат Ло Шу представляет собой таблицу с 3 строками и 3 столбцами
#        (рис. 7 .18). Магический квадрат Ло Шу имеет приведенные ниже свойства:
#   • таблица содержит числа строго от 1 до 9;
#   • сумма каждой строки, каждого столбца и каждой диагонали в итоге составляет одно и то же число (рис. 7 .19).
#        Магический квадрат можно сымитировать в программе при помощи двумерного списка. Напишите функцию, которая
#        принимает двумерный список в качестве аргумента и определяет, не является ли список магическим квадратом Ло Шу.
#        Протестируйте функцию в программе.
# Решение 1:

# def main():
#     S = [[4, 9, 2],
#          [3, 5, 7],
#          [8, 1, 6]]
#
#     if S[0][0] + S[0][1] + S[0][2] == S[1][0] + S[1][1] + S[1][2] \
#             and S[0][0] + S[0][1] + S[0][2] == S[2][0] + S[2][1] + S[2][2] \
#             and S[1][0] + S[1][1] + S[1][2] == S[0][0] + S[0][1] + S[0][2] \
#             and S[1][0] + S[1][1] + S[1][2] == S[2][0] + S[2][1] + S[2][2] \
#             and S[2][0] + S[2][1] + S[2][2] == S[0][0] + S[0][1] + S[0][2] \
#             and S[2][0] + S[2][1] + S[2][2] == S[1][0] + S[1][1] + S[1][2]:
#         print('Данный список является магическм квадратом Ло Шу')
#     else:
#         print('Х**ту написал дружок')
#
#
# main()

# Решение 2:
# lst_in = [[4, 9, 2],
#           [3, 5, 7],
#           [8, 1, 6]]
# horizontal_summ = [sum(i) for i in lst_in]
# vertical_summ = [sum(i) for i in zip(*lst_in)]
# x_sum = [sum([lst_in[num][num] for num, val in enumerate(lst_in)])]
# x_sum2 = [sum(lst_in[num][len(lst_in) - num - 1] for num, val in enumerate(lst_in))]
#
# if len(set(horizontal_summ + vertical_summ + x_sum + x_sum2)) != 1:
#     print('Х**ту написал дружок')
# else:
#     print('Данный список является магическим квадратом Ло Шу')

# - 12 - Генерация простого числа.
#       Напишите программу, которая просит пользователя ввести целое число больше 1 и затем выводит все простые числа,
#       которые меньше или равны введенному числу. Программа должна работать следующим образом:
#   • после того как пользователь ввел число, программа должна заполнить список всеми целыми числами начиная
#       с 2 и до введенного значения;
#   • затем программа должна применить цикл, чтобы пройти по списку. Каждый элемент должен быть в цикле передан в
#       функцию, которая определяет и сообщает, что элемент является простым числом.

# Решение:
# создать ф-ю, передать аргументы
# написать цикл рэйндж 2 до n + 1
# написать вложенный цикл рэйнж от 2 до i
# если i%j==0: break
# else добавить в список
# сделать цикл по листу и вывести все числа с сообщением в ряд что это число простое
# вывести список простых чисел

# def easy_num(l, n):
#
#     for i in range(2, n + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             l.append(i)
#
#     for q in l:
#         print(f'Число {q} простое')
#     print(f'List of simple numbers: {l}')
#
#
# easy_num(l=[], n=int(input(': ')))

# - 13 - Напишите программу, которая моделирует волшебный шар, т. е. игрушку, предсказывающую будущее, которая дает
#        случайный ответ на общий вопрос, требующий ответа "да" или "нет". Программа должна прочитать ответы из файла
#        в список. Она должна предложить пользователю задать вопрос и затем показать один из ответов, отобранных
#        из списка случайным образом. Программа должна продолжать работу до тех пор, пока пользователь не будет готов
#        из нее выйти.
#       Содержимое файла 8 ball responses.txt:
#       Да, разумеется!
#       Вне всяких сомнений, да!
#       Можно рассчитывать, что да.
#       Наверняка.
#       Спросите меня позже.
#       Не уверен.
#       Прямо сейчас не готов сказать.
#       Расскажу после отдыха.
#       Никаких шансов.
#       Не думаю, что будет так.
#       Вне всяких сомнений, нет!
#       Совершенно очевидно, что нет!
# Решение:
# 1- рандом модуль
# 2- открыть файл, прочитать в список
# 3- while true, потом задать вопрос и вывести рандомный ответ
# 4- ретурн функцию.

# import random
#
#
# def func(eight_ball_responses):
#     with open(eight_ball_responses) as text:
#         fail = [i.strip() for i in text.readlines()]
#
#     while True:
#         qestion = input('Задайте вопрос: ')
#         print(random.choice(fail), end='\n' * 2)
#         return func(eight_ball_responses)
#
#
# func('eight_ball_responses.txt')

# - 14 - Круговая диаграмма расходов. Создайте текстовый файл, который содержит ваши расходы за прошлый месяц по
#        приведенным ниже статьям:
#   • арендная плата;
#   • бензин;
#   • продукты питания;
#   • одежда;
#   • платежи по автомашине;
#   • прочие.
#       Напишите программу Python, которая считывает данные из файла и использует пакет matplotlib для построения
#       круговой диаграммы, показывающей, как вы тратите свои деньги.
# Решение:

# import matplotlib.pyplot as plt
#
# def main () :
#
#     sales = [20, 40, 20, 50, 30, 40]
#     slice_labels = ['Арендная плата 20%', 'Бензин 40%', 'Продукты 20%', 'Одежда 50%', 'Платежи по машине 30%\n',
#                     'Прочие 40%']
#     plt.pie(sales, labels=slice_labels)
#     plt.title('Расходы за прошлый месяц')
#     plt.show()
#
#
# main()

# - 15 - График еженедельных цен на бензин за 1994 год. 1994_ Weekly_ Gas_Averages.txt. Этот файл содержит среднюю цену
#        бензина в течение каждой недели 1994 года. (В файле имеется 52 строки.) Используя пакет matplotlib, напишите
#        программу Python, которая считывает содержимое файла и затем строит либо линейный график, либо столбчатую
#        диаграмму. Не забудьте показать содержательные метки вдоль осей х и у, а также метки делений.
# Решение:

# import matplotlib.pyplot as plt
#
# heights = [0.992, 0.995, 1.001, 0.999, 1.005, 1.007, 1.016, 1.009, 1.004, 1.007, 1.005, 1.007, 1.012, 1.011, 1.028, 1.033,
#      1.037, 1.04, 1.045, 1.046, 1.05, 1.056, 1.065, 1.073, 1.079, 1.095, 1.097, 1.103, 1.109, 1.114, 1.13, 1.157,
#      1.161, 1.165, 1.161, 1.156, 1.15, 1.14, 1.129, 1.12, 1.114, 1.106, 1.107, 1.121, 1.123, 1.122, 1.113, 1.117,
#      1.127, 1.131, 1.134, 1.125, 1.136]
# x = range(len(heights))
# ax = plt.gca()
# ax.bar(x, heights, align='edge')
# ax.set_xticks(x)
# plt.title('График еженедельных цен на бензин за 1994 год')
# plt.xlabel ( 'Неделя' )
# plt.ylabel('Цена бензина')
# plt.show()
