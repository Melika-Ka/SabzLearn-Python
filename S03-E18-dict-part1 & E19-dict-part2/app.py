dic1 = {'a': "a", "b": "b"}
print(dic1)
# ---
dic2 = {}
print(type(dic2))
# ---
dic3 = {"name": "melika", "family": "Karimi", "age": 24}
print(dic3["name"])
# مقادیر کلید ها
dic4 = {1: "one", (1, 2, 3): "Hello"}
print(dic4[1])
print(dic4[(1, 2, 3)])
# عدم استفاده از کلید های تکراری
dic5 = {"name": "melika", "family": "Karimi", "age": 24, "age": 26}
print(dic5)
# تغییر مقدار
dic5["age"] = 20
print(dic5)
# add new item
dic5[2] = 30
print(dic5)
#
# print(dic5[3])   # خطا
print(dic5.get("mmm"))  # return None
# methods
# keys() => کلید های دیکشنری را بر میگرداند
print(dic5.keys())
print(type(dic5.keys()))  # dict_keys
# values()
print(dic5.values())
print(type(dic5.values()))  # dict_values
# items()
print(dic5.items())
print(type(dic5.items()))  # dict_items
# حذف عنصر
dic6 = {"name": "Melika", "family": "Karimi", "age": 24, "city": "Teh"}
del dic6["family"]
print(dic6)
# تکنیک عوض کردن کلید
dic7 = {"name": "Melika", "family": "Karimi", "age": 24, "city": "Teh"}
value = dic7["name"]
del dic7["name"]
print(dic7)
dic7["surname"] = value
print(dic7)
# sorted()
l = [4, 8, 12, 0, 7, 5]
print(sorted(l))
print(l)
print(sorted(dic7.keys(), reverse=True))
# تبدیل داده به دیکشنری
dic8 = dict([("a", 2), (2, 1), ("c", 4)])
print(dic8)
dic9 = {x: x ** 2 for x in range(10)}
print(dic9)
# دیکشنری های تو در تو
dic10 = {
    "169": {"name": "a", "id": 1},
    "19": {"name": "z", "id": 2},
    "69": {"name": "f", "id": 3},
    "16": {"name": "ddsf", "id": 4},
}
print(dic10["16"]["name"])
print(dic10["16"]["name"][2])
# in
print("169" in dic10)
print("169" not in dic10)
# is
# zip()
a = [1, 2, 3]
b = "1", "2", "3"
i = zip(a, b)
print(list(i))
