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

'''Write a function that takes a string and returns another function. 
The returned function should take one argument - a 
string s - and return the number of occurrences of the string s in the original string.'''


def str_funk(word):
    def find_str(s):
        return s.count(word)

    return find_str


result = str_funk("word")
print(result('word word wordword'))

'''Write a function that takes one argument - a list of strings, and returns another function. 
The returned function should take one argument - a character c, and return a list of strings from the original list 
that start with the character c.'''


def sp_strok(spisok):
    def one_arg(arg):
        return [i for i in spisok if i.startswith(arg)]

    return one_arg


spisok = ['aim', 'chastiya', 'ayf', 'bar', 'fooboo', 'cok', 'cenaval']
result = sp_strok(spisok)
arg = 'c'
sp_strok = result(arg)
print(sp_strok)

'''Write a function that takes one argument - a list of integers, and returns another function. 
The returned function should take one argument - a number n, and return a list of the first n elements of the original 
list.'''


def sp_digit(spisok):
    def argym(n):
        return spisok[:n]

    return argym


spisok = [12, 1123, 123123, 12424, 23, 42, 2342, 342123, 1, 23, 1231]
result = sp_digit(spisok)
print(result(5))
