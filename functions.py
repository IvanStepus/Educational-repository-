'''Write a function that takes two arguments - numbers a and b - and returns another function.
The returned function should take one argument x and return the result of the expression a * x + b.'''


def numbers(a, b):
    def digit(x):
        return a * x + b

    return digit


result = numbers(3, 5)
print(result(2))

'''Write a function that takes a list of numbers and returns another function.
The returned function should take one argument - a number n - and return the n-th element of the list.'''


def main_func(sp):
    def digit(n):
        return sp[n - 1]

    return digit


sp = [11, 22, 332, 412, 5312, 6321, 7123, 8123, 9112]
result = main_func(sp)
print(result(5))

'''Write a function that takes one argument - a number n - and returns another function.
The returned function should take one argument x and return the result of raising x to the power of n.'''


def degree(n):
    def arg(x):
        return x ** n

    return arg


n = 2
result = degree(n)
print(result(3))

"""Write a function that takes a list of integers as input and returns another function. 
The returned function should take a single argument - a number n - and return the sum of n consecutive 
elements of the list starting from the first element."""


def sp_digit(sp):
    def arg(n):
        return sum(sp[0: n])

    return arg


sp = [9, 8, 7, 6, 5, 4, 3, 2, 1]
result = sp_digit(sp)
print(result(3))
