# # 1
# def function(x):
#     yield x ** 2
#     print("hello")
#
#
# func = function(4)
# print(func.__next__())

# # 2
# def function(x):
#     yield x ** 2
#     print("1")
#     yield x ** 2
#     print("2")
#     yield x ** 2
#     print("3")
#
#
# func = function(4)
# print(func.__next__())
# print(func.__next__())
# print(func.__next__())
# print(func.__next__())

# # 3
# def function():
#     for i in range(10):
#         yield i ** 2
#         print("yield in ok :", i ** 2)
#
#
# generator = function()
# for g in generator:
#     print(g)

# # 4
# # normal function
# def list_range(start, end, step=1):
#     new_range = []
#     while start < end:
#         new_range.append(start)
#         start += step
#     return new_range
#
#
# # generator function
# def generator_range(start, end, step=1):
#     while start < end:
#         yield start
#         start += step
#
#
# range_generator = generator_range(2, 8, 1)
# print(list(range_generator))
#
# range_list = list_range(2, 8, 1)
# print(range_list)

# # 5
#
# # normal function
# def list_range(start, end, step=1):
#     new_range = []
#     while start < end:
#         new_range.append(start)
#         start += step
#     return new_range
#
#
# # generator function
# def generator_range(start, end, step=1):
#     while start < end:
#         yield start
#         start += step
#
#
# # --------------------------------------------------
# from time import perf_counter
#
# start = perf_counter()
# range_generator = generator_range(2, 8, 1)
# print(list(range_generator))
# s = 0
# for i in range_generator:
#     s += i ** 2
# end = perf_counter()
# print("generator time : ", end - start)
# # --------------------------------------------------
#
# range_list = list_range(2, 8, 1)
# print(range_list)
# s = 0
# for i in range_list:
#     s += i ** 2
# print("normal time :", end - start)
# # --------------------------------------------------


# # 6
#
# # normal function
# def list_range(start, end, step=1):
#     new_range = []
#     while start < end:
#         new_range.append(start)
#         start += step
#     return new_range
#
#
# # generator function
# def generator_range(start, end, step=1):
#     while start < end:
#         yield start
#         start += step
#
#
# # --------------------------------------------------
# from time import perf_counter
#
# start_time = perf_counter()
# range_generator = generator_range(1, 100000000000, 1)
# # print(list(range_generator))
# s = 0
# for i in range_generator:
#     if i == 3:
#         break
#     s += i ** 2
# end_time = perf_counter()
# print("generator time : ", end_time - start_time)
# # --------------------------------------------------
# start_time = perf_counter()
# range_list = list_range(1, 10000000000000, 1)
# # print(range_list)
# s = 0
# for i in range_list:
#     if i == 3:
#         break
#     s += i ** 2
# end_time = perf_counter()
# print("normal time :", end_time - start_time)
# # --------------------------------------------------

# # 7
# def my_generator(r):
#     for i in range(r):
#         yield i ** 2
#
#
# generator = my_generator(10)
# for g in generator:
#     if g == 16:
#         generator.close()
#         # generator.throw("Error")
#         # generator.throw("Error")
#     print(g)

# 8
def square_gn(nums):
    for g in nums:
        yield g ** 2


def even_gn(nums):
    for g in nums:
        if g % 2 == 0:
            yield g


print(sum(square_gn(even_gn([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))))
