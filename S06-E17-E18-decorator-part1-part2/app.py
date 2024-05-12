# # exp1
# def dec(func):
#     def inner():
#         print("*" * 20)
#         func()
#
#     return inner
#
#
# def funcs():
#     print("REZA")
#
#
# # funcs()
# call = dec(funcs)
# call()


# # exp2 => شبیه بالا به خط ۲۵ و ۷ نگاه کنید
# def dec(func):
#     def inner():
#         print("*" * 20)
#         func()
#
#     inner()
#
#
# def funcs():
#     print("REZA")
#
#
# # funcs()
# dec(funcs)


# # exp3  => use @function_name
# def dec(func):
#     def inner():
#         print("*" * 20)
#         func()
#
#     return inner
#
#
# @dec
# def funcs():
#     print("REZA")
#
#
# @dec
# def f2():
#     print("hi")
#
#
# funcs()
# f2()

# # exp4 use arguments
# def dec(func):
#     def inner(a, b):
#         if b == 0:
#             print("Warning !!!!!!!!")
#         else:
#             func(a, b)
#
#     return inner
#
#
# @dec
# def funcs(x, y):
#     print(x / y)
#
#
# funcs(3, 2)
# funcs(3, 0)

# # exp5
# def dec(func):
#     def inner(a, b):
#         if b == 0:
#             return "Warning !!!!!!!!"
#         else:
#             return func(a, b)
#
#     return inner
#
#
# @dec
# def funcs(x, y):
#     return x / y
#
#
# print(funcs(3, 2))
# print(funcs(3, 0))


# # exp6

# def dec(func):
#     def inner(*a, **b):
#         if b == 0:
#             return "Warning !!!!!!!!"
#         else:
#             return func(*a, **b)
#
#     return inner
#
#
# @dec
# def funcs(x, y, z):
#     return (x * z) / y
#
#
# print(funcs(3, 2, 5))
# print(funcs(3, 3, 6))

# # exp7
# def dec(func):
#     def inner(*a, **b):
#         print("*")
#         return func(*a, **b)
#
#     return inner
#
#
# @dec
# def msg(name):
#     print("My name is", name)
#
#
# msg("Melika")


# # exp8

# def dec(func):
#     def inner(*a, **b):
#         print("*")
#         return func(*a, **b)
#
#     return inner
#
#
# @dec
# def msg(name):
#     return "My name is " + name
#
#
# print(msg("Melika"))

# # exp9

# def dec(func):
#     def inner(*a, **b):
#         print("*")
#         f = func(*a, **b)
#         print("*")
#         return f
#
#     return inner
#
#
# @dec
# def msg(name):
#     return "My name is " + name
#
#
# print(msg("Melika"))
# # exp10

# def dec(func):
#     def inner(*a, **b):
#         print("*")
#         print(func(*a, **b))
#         print("*")
#
#     return inner
#
#
# @dec
# def msg(name):
#     return "My name is " + name
#
#
# (msg("Melika"))


# # exp11

# def star(func):
#     def inner(*a, **b):
#         print("*")
#         (func(*a, **b))
#         print("*")
#
#     return inner
#
#
# def plus(func):
#     def inner(*a, **b):
#         print("+")
#         (func(*a, **b))
#         print("+")
#
#     return inner
#
#
# def dash(func):
#     def inner(*a, **b):
#         print("-")
#         (func(*a, **b))
#         print("-")
#
#     return inner
#
#
# @plus
# @star
# @dash
# def msg(name):
#     print("My name is " + name)
#
#
# msg("Melika")
# # printer = plus(star(dash(msg)))
# # (printer("hani"))
# # exp12
import functools


def dash(func):
    @functools.wraps(func)
    def inner(*a, **b):
        print("-")
        (func(*a, **b))
        print("-")

    return inner


@dash
def msg(name):
    """meg functions"""
    print("My name is " + name)


print(msg.__name__)
print(msg.__doc__)
