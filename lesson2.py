# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

# from typing import Callable
#
#
# def notebook():
#     todo_list: list[str] = []
#
#     def add_todo(todo: str) -> None:
#         nonlocal todo_list
#         todo_list.append(todo)
#
#     def get_all() -> list[str]:
#         nonlocal todo_list
#         return todo_list
#
#     return add_todo, get_all
#
#
# add, all_todos = notebook()
#
# add('pruvit1')
# add('pruvit2')
# add('pruvit3')
#
# print(all_todos())

# 2) протипізувати перше завдання

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
#  та буде виводити це значення після виконання функцій


# def count_decor(func):
#     count = 0
#
#     def inner(*arks, **kwargs):
#         nonlocal count
#         count += 1
#         res = func(*arks, **kwargs)
#         print(f'{count =}')
#         return res
#
#     return inner

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
#
# @count_decor
# def expanded_form(number: int) -> str:
#     st = str(number)
#     return ' + '.join(ch + '0' * (len(st) - i - 1) for i, ch in enumerate(st) if ch != '0')
#
#
# print(expanded_form(42666))
# print(expanded_form(4264343466))


