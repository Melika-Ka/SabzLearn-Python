# L = [12, 3, 6, 5, 7, 8]
# for i in L:
#     print(i)
# print(range(10))
# print(type(range(10)))
# تبدیل به لیست
# s = list(range(10))
# print(s)

# for i in range(10):
#     print(i)
# # مشخص کردن یک بازه
# for i in range(2, 10):
#     print(i)

# مشخص کردن گام
# for i in range(2, 13, 4):
#     print(i)
# حتی بازه ها و گام میتواند منفی باشد
# for i in range(-2, -13, -4):
#     print(i)
#
# lst = input("names :").split("-")
# for i in lst:
#     print(i)
# for i in range(0, len(lst)):
#     print(i, lst[i])

# پیدا کردن فاکتوریل یک عدد
# n = int(input("Enter n : "))
# for i in range(1, n):
#     n *= i
# print(n)
# معکوس کردن یک عدد

# n = input("Enter : ")
# s = ""
# for i in range(len(n) - 1, -1, -1):
#     s += n[i]
#     print(n[i], end="")
# print()
# print(s)

#
# n = int(input("Enter : "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
# مثلث برعکس بالا
n = int(input("Enter : "))
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
