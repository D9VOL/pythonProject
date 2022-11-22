# Створити клас Rectangle:
# -він має приймати дві сторони x, y
# -описати поведінку на арифметични методи:
#  + сумма площин двох екземплярів ксласу
#  - різниця площин двох екземплярів ксласу
#  == площин на рівність
#  != площин на не рівність
#  >, < меньше більше
#  при виклику метода len() підраховувати сумму сторін

# class Rectangle:
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#
#     def __add__(self, other):
#         return self.x * self.y + other.x * other.y
#
#     def __sub__(self, other):
#         return self.x * self.y - other.x * other.y
#
#     def __eq__(self, other):
#         return self.x * self.y == other.x * other.y
#
#     def __ne__(self, other):
#         return self.x * self.y != other.x * other.y
#
#     def __gt__(self, other):
#         return self.x * self.y > other.x * other.y
#
#     def __lt__(self, other):
#         return self.x * self.y < other.x * other.y
#
#     def __len__(self):
#         return self.x + self.y
#
#
# rectangle1 = Rectangle(2, 3)
# rectangle2 = Rectangle(4, 5)
# print(rectangle1 + rectangle2)
# print(rectangle1 - rectangle2)
# print(rectangle1 == rectangle2)
# print(rectangle1 != rectangle2)
# print(rectangle1 > rectangle2)
# print(rectangle1 < rectangle2)
# print(len(rectangle1))


###############################################################################

# створити класс Human(name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
#  у попелюшки мае бути ім'я, вік, розмір нонги
#  у принца має бути ім'я, вік, та розмір знайденого черевичка,
#  а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cinderella(Human):
#     __count = 0
#
#     def __init__(self, name, age, size):
#         super().__init__(name, age)
#         self.size = size
#         Cinderella.__count += 1
#
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     @classmethod
#     def get_count(cls):
#         print(cls.__count)
#
#
# class Prince(Human):
#     def __init__(self, name, age, find_size):
#         super().__init__(name, age)
#         self.find_size = find_size
#
#     def find_cinderella(self, cinderellas: list[Cinderella]):
#         for cinderella in cinderellas:
#             if cinderella.size == self.find_size:
#                 return cinderella
#         return 'Not Found'
#
#
# cinderellas_list: list[Cinderella] = [
#     Cinderella('Ola', 18, 39),
#     Cinderella('Ira', 21, 37),
#     Cinderella('Julia', 30, 38),
#     Cinderella('Kira', 17, 42),
#     Cinderella('Nela', 25, 35),
# ]
#
# prince = Prince('Vasa', 25, 35)
# print(prince.find_cinderella(cinderellas_list))
# Cinderella.get_count()


###############################################################################

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є
# класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

# from abc import ABC, abstractmethod
#
#
# class Printable(ABC):
#     @abstractmethod
#     def print(self):
#         pass
#
#
# class Book(Printable):
#     def __init__(self, name):
#         self.name = name
#
#     def print(self):
#         print(self.name)
#
#
# class Magazine(Printable):
#     def __init__(self, name):
#         self.name = name
#
#     def print(self):
#         print(self.name)
#
#
# class Main:
#     printable_list: list[Book | Magazine] = []
#
#     @classmethod
#     def add(cls, item: Book | Magazine):
#         if isinstance(item, (Book, Magazine)):
#             cls.printable_list.append(item)
#
#     @classmethod
#     def show_all_magazines(cls):
#         for item in cls.printable_list:
#             if isinstance(item, Magazine):
#                 item.print()
#
#     @classmethod
#     def show_all_books(cls):
#         for item in cls.printable_list:
#             if isinstance(item, Book):
#                 item.print()
#

# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False
