# Можно, но не нужно
# def func(s: str):  # s = s
#     print(s)
#     print(f'{id(s) = }')
#     set_s = set(s)
#     return set_s
#
#
# s = 'hello'
# print(f'{id(s) = }')
# result = func(s)
# print(result)

# Работа механизма share memory
# def func_two(lst: list):  # lst = lst
#     # lst = lst[:]
#     print(lst)
#     print(f'{id(lst) = }')
#     lst.append(1000)
#     set_s = set(lst)
#     return set_s
#
#
# lst = [4, 8, 10]
# print(f'{id(lst) = }')
# result = func_two(lst=lst)
# print(result)
#
# print(f'{lst = }')

# Работа механизма share memory with mutable types
# def func_three(lst: list = [], number=100):  #
#     lst.append(number)
#     return lst
#
#
# gl_lst = [4, 8, 10]
# print(f'{id(gl_lst) = }')
# result = func_three(gl_lst)
# print(result)
#
# result2 = func_three()
# print(result2)  # [100]
#
# result3 = func_three()
# print(result3)  # [100, 100]
#
# result4 = func_three()
# print(result4)  # [100, 100, 100]

# Работа механизма share memory with mutable types
# Как нужно описывать функции по правильному
def good_func(lst=None, number=100):  #
    if lst is None:
        lst = []
    lst.append(number)
    return lst


gl_lst = [4, 8, 10]
print(f'{id(gl_lst) = }')
result = good_func(gl_lst)
print(result)

result2 = good_func()
print(result2)  # [100]

result3 = good_func()
print(result3)  # [100]

result4 = good_func()
print(result4)  # [100]
