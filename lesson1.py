# # strings
#
# # 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# # наприклад:
# # st = 'as 23 fdfdg544' введена строка
# # 2,3,5,4,4        #вивело в консолі.
#
# # st = 'as 23 fdfdg544'
# #
# # print(', '.join([ch for ch in st if ch.isdigit()]))
#
# # 2)написати прогу яка вибирає зі введеної строки числа і виводить їх так як вони написані
# # наприклад:
# #  st = 'as 23 fdfdg544 34' #введена строка
# #  23, 544, 34              #вивело в консолі
#
# # st = 'as 23 fdfdg544 34'
# #
# # print(', '.join(''.join(ch if ch.isdigit() else ' ' for ch in st).split()))
#
# # list comprehension
#
# # 1)є строка:
# # записати кожний символ як окремий елемент списку і зробити його заглавним:
# # ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# #
# # greeting = 'Hello, world'
# #
# # print([ch.upper() for ch in greeting])
#
# # 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# # приклад:
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
# #
# # print([i**2 for i in range(50) if i % 2])
#
# # function
#
# # - створити функцію яка виводить ліст
# # def show(ls):
# #     print(ls)
#
# # - створити функцію яка приймає три числа та виводить та повертає найбільше.
#
# # def max_number(a, b, c):
# #     max1 = max(a, b, c)
# #     print(max1)
# #     return max1
# # max_number(3, 4, -1)
#
# # - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# # def min_max(*args):
# #     print(max(args))
# #     return min(args)
#
# # - створити функцію яка повертає найбільше число з ліста
#
# # def max_of_list(ls):
# #     return max(ls)
#
# # - створити функцію яка повертає найменьше число з ліста
# # def min_of_list(ls):
# #     return min(ls)
#
# # - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# # def sum_of_list(ls):
# #     return sum(ls)
#
# # - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# # def avg(ls):
# #     return sum(ls)/len(ls)
#
# # 1)Дан list:
#
#  # list = [22, 3,5,2,8,2,-23, 8,23,5]
# #  - знайти мін число
#
# def find_min():
#     ls = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#     print(min(ls))
#
# #  - видалити усі дублікати
#
# def set_from_list():
#     ls = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#     print(list(set(ls)))
#
# # - замінити кожне 4-те значення на 'X'
#
# def swap_x():
#     ls = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#     print(['X' if not (i+1)%4 else v for i,v in enumerate(ls)])
#
# # 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
#
# def squere(n):
#     for i in range(n):
#         if i==0 or i==n-1:
#             print('*'*n)
#         else:
#             print('*'+' '*(n-2)+'*')
#
# # 3) вывести табличку множення за допомогою цикла while
#
# def multi_table():
#     i = 1
#     while i <=9:
#         j = 1
#         while j<=9:
#             res = i*j
#             print(f'{res:4}', end='')
#             j+=1
#         i+=1
#         print()
#
# # 4) переробити це завдання під меню
#
# while True:
#     print('1) знайти мін число')
#     print('2) видалити усі дублікати')
#     print('3) замінити кожне 4-те значення на "X"')
#     print('4) вивести на екран пустий квадрат з "*" ')
#     print('5) вывести табличку множення за допомогою цикла while ')
#     print('9) Вихід ')
#
#     choice = input('Зробіть ваш вибір:')
#
#     if choice == '1':
#         find_min()
#     elif choice == '2':
#         set_from_list()
#     elif choice == '3':
#         swap_x()
#     elif choice == '4':
#         squere(6)
#     elif choice == '5':
#         multi_table()
#     elif choice == '9':
#         break
#     print('\n')
#
#
