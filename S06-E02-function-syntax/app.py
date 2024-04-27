# def cube(x):
#     return x ** 3
#
#
# n = cube(3)
# print(cube(9))
# print(cube(14))
# print(cube(20))
# print(n)
#
#
# ##
# def funct():
#     x = input("user input : ")
#     print(int(x) ** 3)
#     # return None #  default
#
#
# # funct()
# print(funct())  # print None


# ##
# def why():
#     x = input("user input : ")
#     return int(x) + 3
#     print("hi")  # اجرا نمیشود
#
#
# print(why())

# rename function name
def cube(x):
    return x ** 3


n = cube
print(n)
print(n(3))
