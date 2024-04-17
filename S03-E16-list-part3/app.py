# append()
list_1 = [1, 4, 6, 7, 8, 9]
list_1.append(5)
print(list_1)
# print(id(list_1))
#
list_1[2:5] = [5, 19, 18]
list_1[2:5] = [5]
print(list_1)
# print(id(list_1))
# del
list_2 = [1, 34]
del list_2[0]
print(list_2)
# len
print(list_1[0:len(list_1)])
#
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)
#
a, b, *c = [1, 3, 6, 7, 9, 3, 8]
print(c)
