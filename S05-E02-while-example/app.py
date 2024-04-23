# برنامه ای که اعدادزوج دو رقمی را بیابید
# n = int(input("Enter n : "))
# while n <= 100:
#     if n % 2 == 0:
#         print(n, " is even")
#     n += 1

# print(30 * "-")
# p = int(input("Enter p : "))
# while p <= 100:
#     if (p % 3 == 0) and (p % 5 == 0):
#         print(p)
#     p += 1


# print(30 * "-")
# row =0
# star = int(input("star"))
# while row <= star:
#     print(star * "*")
#     row += 1


# print(30 * "-")
# # مقسوم علیه های یگ عددرا چاپ کنیم
# num = int(input("Enter your number : "))
# i = 0
# L = []
# while i <= num:
#     i += 1
#     if num % i == 0:
#         L.append(i)
# print(30 * "-")
# # به دست اوردن یک عدد کامل
# if sum(L) - num == num:
#     print("yes")
# else:
#     print("No")

print(30 * "-")
# پرینت سری فوریه
i = 1
a = 0
b = 1
while i <= 20:
    print(a)
    a, b = b, a + b
    i += 1
