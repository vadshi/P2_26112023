"""
1. Напишите функцию декоратор, которая переводит значение декорируемой функции
в рублях, в доллары (курс: 1$ = 90 рубля) или в евро (курс: 1€ = 98 руб).
Как добавить знак валюты:
chr(36) -> '$'
chr(8364) -> '€'
chr(8381) -> '₽'
chr(165) -> '¥'

2*. Добавить возможность передачи параметра(значок валюты) в декоратор.
Найти информацию, разобраться и применить.
Например: @change('$')
"""
RATES = {
    "$": 90,
    "€": 98,
    "¥": 136
}


def change(currency):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = float(function(*args, **kwargs)[:-1])
            new_curr = round(result / RATES[currency], 2)
            return f'{new_curr}{currency}'

        return wrapper

    return decorator


@change('€')
def summa(count: float, price: float) -> str:
    """ Out: <float><CHAR>"""
    return f'{round(count * price, 2):_}₽'


print(summa(305.5, 2.4))
print(summa(1000, price=10))
