# رفتار enumerate را با استفاده از ژنراتور پیادهساز ی کنید.

# print(list(enumerate([5, 2, 3])))
#
#
# def enumerate_gn(nums):
#     i = 0
#     for num in nums:
#         new_enumerate = (i, num)
#         yield new_enumerate
#         i += 1
#
#
# print(list(enumerate_gn([1, 2, 5, 4])))

# # یک ژنراتور برای تولید دنباله فی بوناچی بنویسید.
# def fibu_gn():
#     f1 = 0
#     yield f1
#     f2 = 1
#     yield f2
#     while True:
#         f3 = f2 + f1
#         yield f3
#         f1 = f2
#         f2 = f3
#
#
# fibu = fibu_gn()
# for _ in range(10):
#     print(next(fibu))


# # ژنراتور ی بنوی سید که یک ل یست گرفته و جمع عناصر آن را برگرداند
#
# def sum_gn(nums):
#     sum = 0
#     for num in nums:
#         sum += num
#         yield sum
#
#
# sum_result = sum_gn([1, 2, 3, 5, 7, 8])
# print(list(sum_result))


# # ژنراتور ی بنوی سید که یک رشته گرفته و معکوس آن را برگرداند.
#
# def reverse_gn(str):
#     str_length = len(str)
#     for char in range(str_length - 1, -1, -1):
#         yield str[char]
#
#
# reversed_result = reverse_gn("Melika")
# for char in reversed_result:
#     print(char)

# یک ژنراتور بی نهایت از اعداد زوج یا فرد بنوییسید
# def even_gn(s):
#     while s < 1000:
#         yield s
#         s += 2
#
#
# user_choice = input("Enter odd or even : ")
# if user_choice == "odd":
#     count = even_gn(1)
#     for i in count:
#         print(i)
# elif user_choice == "even":
#     count = even_gn(0)
#     for i in count:
#         print(i)


# ژنراتوری ایجاد کنید که در هر مرحله، خروجی های زیر را تولید کند:
# بار اول : 1
# بار دوم: 2 2
# بار سوم: 3 3 3
def hyrum_gn():
    c = 1
    while True:
        s = ""
        for i in range(1, (c + 1)):
            s += f"{c}\t"
        yield s
        c += 1


result = hyrum_gn()
for _ in range(10):
    print(next(result))

