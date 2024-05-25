# from time import sleep
# decorator

# def decorator(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         print("*" * 40)
#         value = func(*args, **kwargs)
#         print("+" * 40)
#         return value
#
#     return inner
#
#
# @decorator
# def timer(x):
#     sleep(1)
#     if x < 1:
#         print(0)
#         return 0
#     print(x)
#     timer(x - 1)
#
#
# timer(10)


# generator
# def timer_gn(n):
#     sleep(1)
#     if n < 1:
#         return
#     yield n
#     for i in timer_gn(n - 1):
#         yield i
#
#
# g = timer_gn(10)
# print(list(g))

import sys
# set and get recursionlimit()
from time import sleep

# print(sys.getrecursionlimit())


print(sys.setrecursionlimit(10000))

def timer(n):
    # sleep(1)
    if n == 0:
        print(0)
        return
    print(n)
    timer(n - 1)


timer(1000)
