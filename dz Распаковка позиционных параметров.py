# ---------------------------------------------1. Функция с параметрами по умолчанию:

# # Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию
# # (например сейчас это: 1, 'строка', True).
#
#
# def print_params(a = 1, b = 'str', c = True):
# # Функция должна выводить эти параметры.
#     print(a, b ,c)
#
# # Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
# print_params(2, 3 ,4)
# print_params()
# # Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
# print_params(1, 25, c=[1,2,3])

#-----------------------------------------2. Распаковка параметров:


def print_param(a, b, c):
    print(a, b, c)

values_list = [1 ,'str', True] # Создайте список values_list с тремя элементами разных типов.
values_dict = {'a' : 'str', 'b' : True, 'c' : 2} # Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции
                                                 # print_params, и значениями разных типов.
values_list_2 = [54.32, 'Строка']

# Передайте values_list и values_dict в функцию print_params,
# используя распаковку параметров (* для списка и ** для словаря)
print_param(*values_list)
print_param(**values_dict)
print_param(*values_list_2, 42)








