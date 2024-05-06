# 1. تابعی بنویسید که که کار تابع داخلی len را انجام دهد.
# def len_function(a):
#     count = 0
#     for _ in a:
#         count += 1
#     return count
#
#
# user_input = "melika"
# user_input = [1, 2, 3, 4]
# len_result = len_function(user_input)
# print(len_result)

# 2. تابعی بنویسید که کار تابع داخلی max یا min را انجام دهد

# def max_function(*args):
#     max = args[0]
#     for i in args:
#         if i > max:
#             max = i
#     return max
#
#
# max_result = max_function(11, 3, 4, 5, 76, 8, 9, 5424, 1, 12, 435)
# print(max_result)

# 3. تابعی بنویسید که کار تابع داخلی sum را انجام دهد
# def sum_function(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#
#
# sum_function(1, 3, 454, 566778, 9, 86, 765, 23, 2343)
# 4. تابعی بنویسید که که یک عدد به عنوان ورودی گرفته تشخیص دهد عدد مربع است یا خیر

# x = int(input("Enter Your Number : "))


# def square_function(s):
#     square = False
#     for i in range(1, s):
#         if i ** 2 == s:
#             square = True
#             break
#     if square == True:
#         print("Yes")
#     else:
#         print("No")
#
#
# square_function(x)

# 5. تابعی بنویسید که قیمت کالا و درصد تخفیف را گرفته و قیمت پس از تخفیف را محاسبه کند.
# def price_function(price, off_present):
#     total_price = price - (off_present * price / 100)
#     return total_price
#
#
# total_price = price_function(100, 35)
# print(total_price)

# 6. تابعی بنویسید که یک کاراکتر را خوانده و مشخص کند کاراکتر یک رقم، حرف بزرگ، حرف کوچک و یا سایر  نماد ها است