# - 1 - Напишите программу, которая открывает файл вывода my_name.txt, пишет в него ваше имя и затем его закрывает.

# Решение:
# def main():
#     my_fale = open('my_name.txt', 'w')
#     my_fale.write('Anton')
#     my_fale.close()
# main()

# - 2 - Напишите программу, которая открывает файл my_name.txt, созданный программой в задаче
#       1, читает ваше имя из файла, выводит имя на экран и затем закрывает файл.

# Решение:
# def main():
#     my_fale = open('my_name.txt', 'r')
#     line1 = my_fale.readline()
#     my_fale.close()
#     print(line1)
# main()

# - 3 - Напишите программу, которая делает следующее: открывает выходной файл с именем number_list.txt, применяет
#       цикл для записи в файл чисел с 1 по 100, а затем закрывает файл.

# Решение:
# def main():
#     number_file = open('number_list.txt', 'w')
#     for i in range(101):
#         number_file.write(str(i) + '\n')
#     number_file.close()
# main()

# - 4 - Напишите программу, которая делает следующее: открывает файл number_list.txt, созданный программой,
#       которую вы написали в задаче 3, читает все числа из файла, выводит их на экран и затем закрывает файл.

# Решение:
# def main():
#    number_file = open('number_list.txt', 'r')
#    for i in number_file:
#        amount = int(i)
#        print(format(amount))
#    number_file.close()
# main()

# - 5 - Измените программу, которую вы написали в задаче 4 таким образом, чтобы она суммировала
#       все прочитанные из файла числа и выводила на экран их сумму.

# Решение:
# def main():
#     number_file = open('number_list.txt', 'r')
#     total = 0
#     for i in number_file:
#         count = int(i)
#         total += count
#     number_file.close()
#     print('Сумма = ', total)
# main()

# - 6 - Напишите программу, которая открывает файл вывода number_list.txt, но не стирает содержимое
#       файла, если он уже существует.

# Решение:
# def main():
#     number_file = open('number_list.txt', 'a')
#     number_file.close()
# main()

# - 7 - На диске существует файл students. txt. Он содержит несколько записей, и каждая запись
#       имеет два поля: имя студента и оценку студента за итоговый экзамен. Напишите программу,
#       которая удаляет запись с именем студента "Джон Перц".

# Решение:
# import os
#
# def main () :
#     found = False
#     search = input('Kaкие данные удалить? ')
#     coffee_file = open('students.txt', 'r')
#     temp_file = open('temp.txt', 'w')
#     descr = coffee_file.readline()
#     while descr != '':
#         qty = float(coffee_file.readline())
#         descr = descr. rstrip ( '\n')
#         if descr != search:
#             temp_file.write(descr + '\n')
#             temp_file.write(str(qty) + '\n')
#         else:
#             found = True
#         descr = coffee_file.readline()
#     coffee_file.close()
#     temp_file.close()
#     os. remove('students.txt')
#     os. rename('temp.txt', 'students.txt')
#     if found:
#         print('Фaйл обновлен.')
#     else:
#         print('Этo значение в файле не найдено.')
# main ()


# - 8 - На диске существует файл students.txt. Он содержит несколько записей, и каждая запись имеет два поля:
#       имя студента и оценку студента за итоговый экзамен. Напишите программу, которая меняет оценку
#       Джулии Милан на 100.

# Решение:
# import os
#
# def main():
#     found = False
#     search = input('Введите Имя: ')
#     new_qty = int(input('Введиное новую оценку: '))
#     coffee_file = open('students.txt', 'r')
#     temp_file = open('temp.txt', 'w')
#     descr = coffee_file.readline()
#
#     while descr != '':
#         qty = float(coffee_file.readline())
#         descr = descr.rstrip('\n')
#
#         if descr == search:
#
#             temp_file.write(descr + '\n')
#             temp_file.write(str(new_qty) + '\n')
#             found = True
#
#         else:
#             temp_file.write(descr + '\n')
#             temp_file.write(str(qty) + '\n')
#         descr = coffee_file.readline()
#     coffee_file.close()
#     temp_file.close()
#     os.remove('students.txt')
#     os.rename('temp.txt', 'students.txt')
#
#     if found:
#         print('Файл обновлен.')
#     else:
#         print('Это значение в файле не найдено.')
# main()



























































