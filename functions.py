'''Напишите функцию, которая принимает два аргумента - числа a и b, и возвращает другую функцию.
Возвращаемая функция должна принимать один аргумент x и возвращать результат выражения a * x + b.'''


def numbers(a, b):
    def digit(x):
        return a * x + b
    return digit
result = numbers(3, 5)
print(result(2))

'''Напишите функцию, которая принимает список чисел и возвращает другую функцию. 
Возвращаемая функция должна принимать один аргумент - число n, и возвращать n-ый элемент списка.'''


def main_func(sp):
    def digit(n):
        return sp[n - 1]
    return digit
sp = [11, 22, 332, 412, 5312, 6321, 7123, 8123, 9112]
result = main_func(sp)
print(result(5))