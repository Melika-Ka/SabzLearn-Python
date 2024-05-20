# # 1
#
# def my_gn():
#     print("Start")
#     while True:
#         yield 1
#         print("Ok")
#
#
# g = my_gn()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# # 2
# def my_gn():
#     print("Start!")
#     while True:
#         name = yield
#         print("My name is ", name)
#
#
# g = my_gn()
# print(next(g)) # None

# # 3
#
# def my_gn():
#     print("Start!")
#     while True:
#         name = yield 1
#         print("My name is ", name)
#
#
# g = my_gn()
# # next(g)
# print(next(g))
# print(g.send("Melika"))

# # 4
# def my_gn():
#     print("Hi")
#     for i in range(10):
#         name = yield i
#         print("My name is", name)
#
#
# g = my_gn()
# print(next(g))
# print(g.send("Melika"))
# print(g.send("Neda"))
# print(g.send("Hani"))
# print(g.send("Ali"))
# print(g.send("Yasi"))

# 5
from functools import wraps


def coroutine(func):
    @wraps(func)
    def start(*args, **kwargs):
        gn = func()
        print(next(gn))
        return gn

    return start


@coroutine
def my_gn():
    print("Hi")
    for i in range(10):
        name = yield i
        print("My name is", name)


g = my_gn()
print(g.send("Melika"))
print(g.send("Eli"))
print(g.send("Hani"))
