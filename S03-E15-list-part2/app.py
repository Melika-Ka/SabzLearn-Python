lis_1 = [1, 344, 7, 90, -9, 6545, 3455]
lis_2 = lis_1
print(id(lis_1), "---", id(lis_2))
# # ---
lis_2[3] = 33
print(lis_1)
print(id(lis_1), "---", id(lis_2))

# # راه حل ۱ بالا : کپی اولی را در دومی قرار دهیم
lis_4 = lis_1[:]
print(id(lis_1), "---", id(lis_4))
lis_4[3] = 88
print(lis_1)
print(id(lis_1), "---", id(lis_4))

# راه حل ۲ بالا : استفاده از متد copy
lis_3 = lis_1.copy()
print(id(lis_1), "---", id(lis_3))
# لیست ها میتوانند شامل لیست هم باشند
lis_5 = [1, 2, ["ali", "b"]]
print(lis_5[2])
print(lis_5[2][0][1])
#
lis_6 = lis_5.copy()
print(id(lis_5))
print(id(lis_6))
lis_6[2][0] = "hani"
print(lis_5)
print(lis_6)
#
lis_7 = lis_5.copy()
# کپی سطحی

import copy

lis_8 = copy.copy(lis_5)
lis_8[2][0] = "melik"
print(lis_5)
print(lis_8)
# کپی عمیق
lis_9 = copy.deepcopy(lis_5)
lis_9[2][0] = "Amir"
print(lis_5)
print(lis_9)
