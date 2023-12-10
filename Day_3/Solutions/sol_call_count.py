# Как с помощью атрибутов функции посчитать количество вызовов этой функции?
def func_v1(a=5, b=8):
    try:
        func_v1.counter += 1
    except:
        func_v1.counter = 1
    return a + b


def func_v2(a=5, b=8):
    if not hasattr(func_v2, 'counter'):
        func_v2.counter = 0
    func_v2.counter += 1
    return a + b


# Первый вариант
# func.counter = 0
print(func_v1())
print(func_v1(10, 20))
print(func_v1())
print(func_v1(4, 9))
print(func_v1.counter)