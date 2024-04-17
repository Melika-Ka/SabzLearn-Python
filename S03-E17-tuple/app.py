my_tuple = (1, 2, 3, "Reza", [1, 2], (1, 2))
my_tuple_2 = 1, 2, 3, [1, 2]
print(my_tuple_2)
print(type(my_tuple_2))
# استفاده از عملگر جمع
# استفاده از عملگر ضرب
# سلکت کردن
# انتخاب بازه ای
# لیست داخل تاپل
tuple_1 = (1, 2, 3, [1, 3, 5])
tuple_1[3][1] = 4
print(tuple_1)
# len()
# empty tuple
empty_tuple = ()
print(type(empty_tuple))
tuple_2 = (2)
print(tuple_2)
print(type(tuple_2))  # return int
tuple_3 = (2,)
print(tuple_3)
print(type(tuple_3))
# ---
list_1 = [1]
print(list_1)
print(type(list_1))  # return list
# تبدیل رشته به تاپل
txt = "Amir"
print(tuple(txt))
print(type(tuple(txt)))
# how to change tuple
tuple_4 = (1, 3, 6)
tuple_to_list = list(tuple_4)
tuple_to_list[1] = 7
list_to_tupple = tuple(tuple_to_list)
print(list_to_tupple)
# ---
t = "(1, 3, 4567, 878, 57, 435, 23, 12)"
x, *y, z = t
print(y)
print(type(y))
print(type(x))

# کپی سطحی
t1 = (1, 2, 3, [1, 2, 6])
t2 = t1[:]
# t2 = t1
print(id(t1))
print(id(t2))
t2[3][1] = 7
print(t1)

import copy

t3 = copy.copy(t1)
t3[3][2] = 10
print(t1)

# کپی عمیق

t4 = copy.deepcopy(t1)
t4[3][2] = 9
print(t1)
