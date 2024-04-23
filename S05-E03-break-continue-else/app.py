# break
# i = int(input("enter * count : "))
# n = 1
# while n <= i:
#     print(i * "*")
#     if (i == 6):
#         break
#     i -= 1

# # تعدادی عدد و کچک ترین آن
# n = int(input("n : "))
# # mimi = float("inf")
# mini = n
# while True:
#     is_continue = input("do you want  continue ? (yes or no)")
#     if is_continue.lower() == "yes":
#         n = int(input("n : "))
#         if mini < n:
#             pass
#         else:
#             mini = n
#     else:
#         break
# print(mini, " is smallest number")

# continue
# پرینت اعدادی که بر سه بخش پٔیر نیستند
# i = int(input("enter * count : "))
# n = 1
# while n <= i:
#     i -= 1
#     if i % 3 == 0:
#         continue
#     print(i)

# else
# i = int(input("enter * count : "))
# n = 1
# while n <= i:
#     i -= 1
#     if i % 3 == 0:
#         continue
#     print(i)
# else:
#     print("finishing Ok")
# عدد اول را تشخیص دهیم

i = int(input("enter i :"))
n = 2
if i == 1:
    print("Enter correct number")
else:
    while n < i:
        if i % n == 0:
            print(n, " not prime")
            break
        n += 1
    else:
        print("yes is prime")
