# 1 - class Pet:
# class Pet:
#
#     def __init__(self, name, animal_type, age):
#         self.__name = name
#         self.__animal_type = animal_type
#         self.__age = age
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_animal_type(self, animal_type):
#         self.__animal_type = animal_type
#
#     def set_age(self, age):
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_animal_type(self):
#         return self.__animal_type
#
#     def get_age(self):
#         return self.__age
#
#
# s = Pet(input('Name: '), input('AnimalType: '), int(input('Age: ')))
# print(f'Name: {s.get_name()}\nType: {s.get_animal_type()}\nAge: {s.get_age()}')


# 2 - class Car
# class Car:
#
#     def __init__(self, year_model, make):
#         self.__year_model = year_model
#         self.__make = make
#         self.__speed = 0
#
#     def accelerate(self):
#         self.__speed += 5
#
#     def breack(self):
#         self.__speed -= 5
#
#     def get_speed(self):
#         return self.__speed
#
#
# car = Car(int(input('Год: ')), input('Фирма: '))
#
# for i in range(1, 6):
#     car.accelerate()
#     print(car.get_speed())
# for j in range(1, 6):
#     car.breack()
#     print(car.get_speed())


# 3 - class Infoпnation
# class Information:
#
#     def __init__(self, name, address, age, phone_num):
#         self.__name = name
#         self.__address = address
#         self.__age = age
#         self.__phone_num = phone_num
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_address(self, address):
#         self.__address = address
#
#     def set_age(self, age):
#         self.__age = age
#
#     def set_phone_num(self, phone_num):
#         self.__phone_num = phone_num
#
#     def get_name(self):
#         return self.__name
#
#     def get_address(self):
#         return self.__address
#
#     def get_age(self):
#         return self.__age
#
#     def get_phone_num(self):
#         return self.__phone_num
#
#
# anton = Information('Anton', 'SosnovyBor', '28', '13241234')
# masha = Information('Masha', 'SosnovyBor', '26', '23141234')
# jeka = Information('Jeka', 'SosnovyBor', '2', '-')
# print(f'Имя: {anton.get_name()}\nАдрес: {anton.get_address()}\n'
#       f'Возраст: {anton.get_age()}\nТелефон: {anton.get_phone_num()}')
# print()
# print(f'Имя: {masha.get_name()}\nАдрес: {masha.get_address()}\n'
#       f'Возраст: {masha.get_age()}\nТелефон: {masha.get_phone_num()}')
# print()
# print(f'Имя: {jeka.get_name()}\nАдрес: {jeka.get_address()}\n'
#       f'Возраст: {jeka.get_age()}\nТелефон: {jeka.get_phone_num()}')


# 4 - class Employee.
# class Employee:
#
#     def __init__(self, name, id_num, otdel, dolj):
#         self.__name = name
#         self.__id_num = id_num
#         self.__otdel = otdel
#         self.__dolj = dolj
#
#     def get_name(self):
#         return self.__name
#
#     def get_id_num(self):
#         return self.__id_num
#
#     def get_otdel(self):
#         return self.__otdel
#
#     def get_dolj(self):
#         return self.__dolj
#
#
# def get_info() -> list:
#     lst = []
#     for i in range(1, 4):
#         name = input('Имя: ')
#         id_num = input('Номер ID: ')
#         otdel = input('Отдел: ')
#         dolj = input('Должность: ')
#         print()
#         s = Employee(name, id_num, otdel, dolj)
#         lst.append(s)
#     return lst
#
#
# if __name__ == '__main__':
#     result = get_info()
#     print('Наши данные')
#
#     for line in result:
#         print()
#         print(f'Имя: {line.get_name()}\n'
#               f'Номер ID: {line.get_id_num()}\n'
#               f'Отдел: {line.get_otdel()}\n'
#               f'Должность: {line.get_dolj()}')


# 5 - class Retailitem.
# class RetailItem:
#
#     def __init__(self, product_description, quantity, price):
#         self.__product_description = product_description
#         self.__quantity = quantity
#         self.__price = price
#
#     def get_product_description(self):
#         return self.__product_description
#
#     def get_quantity(self):
#         return self.__quantity
#
#     def get_price(self):
#         return self.__price
#
#     def __str__(self):
#         return f'Товар: {self.get_product_description()}\t\t' \
#                f'Количество на складе: {self.get_quantity()}\t\t' \
#                f'Цена: {self.get_price()}'
#
#
# product_1 = RetailItem('Пиджак', 12, 59.95)
# product_2 = RetailItem('Дизайнерские джинсы', 40, 34.95)
# product_3 = RetailItem('Рубашка', 20, 24.95)
# print(f'\n{product_1}\n'
#       f'\n'
#       f'{product_2}\n'
#       f'\n'
#       f'{product_3}')


# 6 - Расходы на лечение.
# class Patient:
#
#     def __init__(self, f_name, m_name, l_name, address, city,
#                  oblast, post_index, phone_number, second_name, second_phone):
#         self.__f_name = f_name
#         self.__m_name = m_name
#         self.__l_name = l_name
#         self.__addres = address
#         self.__city = city
#         self.__oblast = oblast
#         self.__post_index = post_index
#         self.__phone_number = phone_number
#         self.__second_name = second_name
#         self.__second_phone = second_phone
#
#     def set_f_name(self, f_name):
#         self.__f_name = f_name
#
#     def set_m_name(self, m_name):
#         self.__m_name = m_name
#
#     def set_l_name(self, l_name):
#         self.__l_name = l_name
#
#     def set_address(self, address):
#         self.__addres = address
#
#     def set_city(self, city):
#         self.__city = city
#
#     def set_oblast(self, oblast):
#         self.__oblast = oblast
#
#     def set_post_index(self, post_index):
#         self.__post_index = post_index
#
#     def set_phone_number(self, phone_number):
#         self.__phone_number = phone_number
#
#     def set_second_name(self, second_name):
#         self.__second_name = second_name
#
#     def set_second_phone(self, second_phone):
#         self.__second_phone = second_phone
#
#     def get_f_name(self):
#         return self.__f_name
#
#     def get_m_name(self):
#         return self.__m_name
#
#     def get_l_name(self):
#         return self.__l_name
#
#     def get_address(self):
#         return self.__addres
#
#     def get_city(self):
#         return self.__city
#
#     def get_oblast(self):
#         return self.__oblast
#
#     def get_post_index(self):
#         return self.__post_index
#
#     def get_phone_number(self):
#         return self.__phone_number
#
#     def get_second_name(self):
#         return self.__second_name
#
#     def get_second_phone(self):
#         return self.__second_phone
#
#     def __str__(self):
#         return f'First Name: {self.get_f_name()}\n' \
#                f'Middle Name: {self.get_m_name()}\n' \
#                f'Last Name: {self.get_l_name()}\n' \
#                f'Address: {self.get_address()}\n' \
#                f'City: {self.get_city()}\n' \
#                f'Oblast: {self.get_oblast()}\n' \
#                f'Post Index: {self.get_post_index()}\n' \
#                f'Phone Number: {self.get_phone_number()}\n' \
#                f'Extra Name: {self.get_second_name()}\n' \
#                f'Extra Phone: {self.get_second_phone()}'
#
#
# patient = Patient('Anton', 'Chupriyanov', 'Evgenievith', 'Mash2', 'SosnovyBor',
#                   'Leningradskaya', '188544', '9214124122', 'Maria', '9554322121')
# print(f'- > ПАЦИЕНТ < - \n\n{patient}')
#
#
# class Procedure:
#
#     def __init__(self, name_proc, data, name_doctor, price):
#         self.__name_proc = name_proc
#         self.__data = data
#         self.__name_doctor = name_doctor
#         self.__price = price
#
#     def set_name_proc(self, name_proc):
#         self.__name_proc = name_proc
#
#     def set_data(self, data):
#         self.__data = data
#
#     def set_name_doctor(self, name_doctor):
#         self.__name_doctor = name_doctor
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_name_proc(self):
#         return self.__name_proc
#
#     def get_data(self):
#         return self.__data
#
#     def get_name_doctor(self):
#         return self.__name_doctor
#
#     def get_price(self):
#         return self.__price
#
#     def __str__(self):
#         return f'\nНазвание процедуры:\n{self.get_name_proc()}\t' \
#                f'Дата процедуры: {self.get_data()}\t' \
#                f'Врач: {self.get_name_doctor()}\t' \
#                f'Стоимость: {self.get_price()}'
#
#
# print()
# procedure_1 = Procedure('врачебный осмотр--> ', 'сегодняшняя ', 'Ирвин,', 250.00)
# procedure_2 = Procedure('рентгеноскопия--> ', 'сегодняшняя ', 'Джемисон, ', 500.00)
# procedure_3 = Procedure('анализ крови--> ', 'сегодняшняя ', 'Смит, ', 200.00)
# print(f'{procedure_1}\n{procedure_2}\n{procedure_3}\n'
#       f'\nОбщая стоимость процедур: '
#       f'$ {procedure_1.get_price() + procedure_2.get_price() + procedure_3.get_price()}')

# 7 - Система управления персоналом.
# from pickle import dump, load
#
#
# class Employee:
#
#     def __init__(self, name, id_num, departament, job_title):
#         self.__name = name
#         self.__id_num = id_num
#         self.__departament = departament
#         self.__job_title = job_title
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_id_num(self, id_num):
#         self.__id_num = id_num
#
#     def set_departament(self, departament):
#         self.__departament = departament
#
#     def set_job_title(self, job_title):
#         self.__job_title = job_title
#
#     def get_name(self):
#         return self.__name
#
#     def get_id_num(self):
#         return self.__id_num
#
#     def get_departament(self):
#         return self.__departament
#
#     def get_job_title(self):
#         return self.__job_title
#
#     def __str__(self):
#         return f'Name: {self.__name}\nID: {self.__id_num}\n' \
#                f'Departament: {self.__departament}\nJob Title: {self.__job_title}'
#
#
# LOOK_UP = 1
# ADD = 2
# CHANGE = 3
# DELETE = 4
# QUIT = 5
# FILENAME = 'employes.dat'
#
#
# def main():
#     # Загрузить существующий словарь контактов и присвоить его переменной mycontacts.
#     my_contacts = load_contacts()
#     # Инициализировать переменную для выбора пользователя.
#     choice = 0
#     # Обрабатывать варианты выбора пунктов меню до тех пор, пока пользователь не пожелает выйти из программы.
#     while choice != QUIT:
#         # Получить выбранный пользователем пункт меню.
#         choice = get_menu_choice()
#         if choice == LOOK_UP:
#             look_up(my_contacts)
#         elif choice == ADD:
#             add(my_contacts)
#         elif choice == CHANGE:
#             change(my_contacts)
#         elif choice == DELETE:
#             delete(my_contacts)
#
#     save_contacts(my_contacts)
#
#
# def load_contacts():
#     try:
#         with open(FILENAME, 'rb') as file:
#             # Расконсервировать словарь.
#             contact_dct = load(file)
#     except IOError:
#         # Не получипось открыть файл, поэтому создать пустой словарь.
#         contact_dct = {}
#
#     return contact_dct
#
#
# def get_menu_choice():
#     print()
#     print(f'Меню\n{"-" * 30}\n'
#           f'1. Найти контактное лицо.\n'
#           f'2. Добавить новое контактное лицо\n'
#           f'3. Изменить существующее контактное лицо\n'
#           f'4. Удалить контактное лицо\n'
#           f'5. Выйти из программы', end='\n')
#
#     choice = int(input('Введите выбранный пункт: '))
#     while LOOK_UP > choice > QUIT:
#         choice = int(input('Введите выбранный пункт: '))
#     return choice
#
#
# def look_up(my_contacts):
#     name = input('Введите имя: ')
#     print(f'{my_contacts.get(name, "Это имя не найдено.")}')
#
#
# def add(my_contacts):
#     name, id_num, departament, job_title = input('Имя: '), input('Идентификационный номер: '),\
#                                            input('Отдел: '), input('Должность: ')
#     entry = Employee(name, id_num, departament, job_title)
#     if name not in my_contacts:
#         my_contacts[name] = entry
#         print('Запись добавлена')
#     else:
#         print('Это имя уже существует')
#
#
# def change(my_contacts):
#     name = input('Введите имя: ')
#     if name in my_contacts:
#         id_num = input('Введите новый идентификационный номер: ')
#         departament = input('Введите новый отдел: ')
#         job_title = input('Введите новую должность: ')
#         entry = Employee(name, id_num, departament, job_title)
#
#         my_contacts[name] = entry
#         print('Информация обновлена')
#     else:
#         print('Это имя не найдено')
#
#
# def delete(my_contacts):
#     name = input('Введите имя: ')
#     if name in my_contacts:
#         del my_contacts[name]
#         print('Запись удалена')
#     else:
#         print("Имя не найдено")
#
#
# def save_contacts(my_contacts):
#     with open(FILENAME, 'wb') as file:
#         dump(my_contacts, file)
#
#
# main()


# 8 -class RetailItem
# class RetailItem:
#     def __init__(self, description, units, price):
#         self.__description = description
#         self.__units = units
#         self.__price = price
#
#     def set_description(self, description):
#         self.__description = description
#
#     def set_units(self, units):
#         self.__units = units
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_description(self):
#         return self.__description
#
#     def get_UI(self):
#         return self.__units
#
#     def get_price(self):
#         return float(self.__price)
#
#
# class CashRegister:
#     def __init__(self):
#         self.__list = []
#
#     def purchase_item(self, item):
#         self.__list.append(item)
#
#     def get_total(self):
#         count = 0.0
#         for line in self.__list:
#             count += line.get_price()
#         return count
#
#     def show_items(self):
#         for line in self.__list:
#             print(line.get_description())
#
#     def clear(self):
#         return self.__list.clear()
#
#
# product_1 = RetailItem('Jac', 12, 59.95)
# product_2 = RetailItem('Jea', 40, 34.95)
# product_3 = RetailItem('Lock', 20, 24.95)
# cash = CashRegister()
# print(f'Выберите товар из списка:\n'
#       f'{product_1.get_description()}\n'
#       f'{product_2.get_description()}\n'
#       f'{product_3.get_description()}')
#
# start = 'y'
# while start != 'n':
#
#     items = input('Введите товар сюда >: ')
#     if items == product_1.get_description():
#         cash.purchase_item(product_1)
#     elif items == product_2.get_description():
#         cash.purchase_item(product_2)
#     elif items == product_3.get_description():
#         cash.purchase_item(product_3)
#     else:
#         print('Таких товаров у нас нет')
#
#     start = input('Ввести ещё товар ? "y" если да, "n" если нет: ')
# print(f'Товары которые вы купили: ')
# cash.show_items()
# print('Сумма товаров')
# print(cash.get_total())


# 9 - Викторина.
# class Question:
#   pass


# 10 - class Dice: ---------------- ne reshena
from random import randint


class Dice:
    def __init__(self):
        self.history = []

    def dice_throw(self):

        return randint(1, 121)

    def get_history(self, x=4):
        if len(self.history) > 5:
            return self.history[-x:]
        return self.history


dice_4 = Dice()
dice_4.history.append(dice_4.dice_throw())
print(dice_4.dice_throw())
print(dice_4.get_history())


# 11 - Повышение уровня
# class Hero:
#
#     def __init__(self, name, health=100, experience=0, level=1):
#         self.name = name
#         self.health = health
#         self.experience = experience
#         self.level = level
#
#     def add_experience(self):
#         """добавляет опыт, при этом уровень и здоровье пересчитываются."""
#         return
#
#     def get_level(self):
#         """возвращает опыт, это целое число."""
#         self.level += 1
#
#     def get_health(self) -> int:
#         """возвращает здоровье, это целое число."""
#         return (10 - self.health % 10) + self.health
#
#
# hero = Hero('Jeka')















