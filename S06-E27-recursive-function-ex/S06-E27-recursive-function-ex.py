# import time
#
#
# # timer
# def timer_recursive(x):
#     time.sleep(1)
#     if x == 0:
#         print(x)
#         return
#     print(x)
#     timer_recursive(x - 1)
#
#
# timer_recursive(6)

# #
# def mul(x):
#     if x == 0:
#         return 1
#     elif x % 10 < 5:
#         return mul(x // 10)
#     else:
#         return x % 10 * mul(x // 10)
#
#
# print(mul(5))
#
# print(mul(14356))

# #
# def func(x):
#     if x <= 1:
#         return
#     elif x % 3 == 0:
#         print(x)
#     func(x - 1)
#
#
# func(9)

# fibu
def fibu_function(x):
    if x == 0 or x == 1:
        return x
    return fibu_function(x - 1) + fibu_function(x - 2)


# 5 => 0 1 1 2 3 5
# 3 => 2 + 1=> 1 + 0 + 1
print(fibu_function(7))
