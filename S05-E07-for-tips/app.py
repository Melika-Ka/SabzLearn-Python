# enumerate([1, 2, 3, 4])
# print(enumerate([1, 2, 3, 4]))
# print(list(enumerate([1, 2, 3, 4])))

##
# lst = [1, 2, 3, 4, 5, 7, 8]
# for i, j in enumerate(lst):
#     print(i, j)
# print(30 * "//")
# # اندیس گذاری
# for i, j in enumerate(lst, 10):
#     print(i, j)
# zip
x = ["ali", "mina", "amir"]
y = [21, 23, 43]
for i, j in zip(x, y):
    print("name : ", i, " - age : ", j)
    print(20 * "+")
# reversed
for i in reversed(x):
    print(i)
print(20 * "..")
for i in sorted(x):
    print(i)
print(20 * "..")
for i in reversed(sorted(y)):
    print(i)
print(20 * "..")
for i in sorted(y, reverse=True):
    print(i)
