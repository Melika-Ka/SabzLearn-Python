# func = lambda parameters1, parameters2: parameters1 ** parameters2
# print(func(2, 3))

# map

# function = lambda x: x ** 2
# li = [1, 2, 3, 4]
# print(li)
# # map_result = list(map(function, li))
# map_result = list(map(lambda x: x ** 2, li))
# print(map_result)
# print(li)

# # filter()

# # def filter_function(x):
# #     if x > 5:
# #         return True
#
#
# filter_function = lambda x: x > 5
#
# li = [1, 234, 65, 8, 9, 5, 25, 9, -1, 2, 34, 75, 97]
# filter_result = list(filter(filter_function, li))
# print(filter_result)

# # reduce()

# # def reduce_function(x, y):
# #     return x + y
# reduce_function = lambda x, y: x + y
#
# li = [1, 2, 3, 4, 5, 6, 7]
# reduce_result = (reduce(reduce_function, li))
# print(reduce_result)

# sorted()
li = [1, 4, 7, 9, 23, 56, 78, 2, 2, 3, 6]
li2 = ["asdd", "a", "A", "adsfdgdfg"]
sorted_result = sorted(li)
sorted_result = sorted(li2, key=len)
print(sorted_result)
