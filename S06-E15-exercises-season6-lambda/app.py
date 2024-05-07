# 1. برنامه ای بنویسید که با استفاده از لامبدا، اعداد زوج و فرد را در یک لیست از اعداد صحیح بشمارد
lst = [1, 2, 4, 6, 8, 2, 5, 7, 3, 235, 57, 8, 45]
print(lst)
even_function = lambda x: x % 2 == 0
odd_function = lambda x: x % 2 != 0
even_result = len(list(filter(even_function, lst)))
odd_result = len(list(filter(odd_function, lst)))
print(even_result)
print(odd_result)

# 2. لیست ی از تاپل ها به شکل ]... , (65′ ,‘Reza(,) 93′ ,’Ali ](دار یم. با استفاده از لامبدا
#  برنامه ای بنویسید که این لیست را بر اساس اعداد موجود در تاپل مرتب کند.
lst = [("Reza", 55), ("Ali", 15), ("Mohammad", 76)]
sort_function = lambda x: x[1]
sort_result = sorted(lst, key=sort_function, reverse=True)
print(sort_result)

# 3. لیست ی از دیکشنری ها به شکل ]... , :‘apple ‘50, :’weight{ {‘red ]‘دار یم. با استفاده از
#    لامبدا برنامه ای بنویسید که این ل یست را بر اساس رنگ موجود در دیکشنری مرتب کند.
lst = [
    {"weight": 22, "color": "blue"},
    {"weight": 22, "color": "red"},
    {"weight": 22, "color": "green"},
    {"weight": 22, "color": "orange"},
    {"weight": 22, "color": "yellow"},
    {"weight": 22, "color": "white"}
]
sort_function = lambda x: x["color"]
sort_result = sorted(lst, key=sort_function)
print(sort_result)

# 4. برنامه ای بنویسید تا لیستی از اعداد صح یح را با استفاده از لامبدا به زوج ها و فردها فیلتر کند.
lst = [1, 2, 4, 6, 8, 2, 5, 7, 3, 235, 57, 8, 45]
print(lst)
even_function = lambda x: x % 2 == 0
odd_function = lambda x: x % 2 != 0
even_result = (list(filter(even_function, lst)))
odd_result = (list(filter(odd_function, lst)))
print(even_result)
print(odd_result)
# 5. با استفاده از لامبدا یک برنامه ای بنویسید تا هر عدد را در لیستی از اعداد صحیح مربع و مکعب کند.
lst = [1, 2, 4, 6, 8, 2, 5, 7, 3, 235, 57, 8, 45]
square_function = lambda x: x ** 2
cube_function = lambda x: x ** 3

square_result = list(map(square_function, lst))
cube_result = list(map(cube_function, lst))
print(square_result)
print(cube_result)

# 6. با استفاده از لامبدا برنامه ای بنویسید تا بفهمید که آیا یک رشته داده شده با یک کاراکتر مشخص
#    شروع می شود یا خیر
name = "Reza"
start_with_function = lambda x: True if x.startswith("R") else False
print(start_with_function(name))
# 7. با استفاده از لامبدا برنامه ای بنویسید تا بررسی کند که آیا یک رشته داده شده عددی است یا خیر.
#    )توجه داشته باشید که میخواهیم رشته های اعشاری همچون ”4.5“ هم تشخیص داده شوند.
is_number_function = lambda x: x.replace(".", "", 1).isdigit()
print(is_number_function("123.344"))
print(is_number_function("dggfg"))
print(is_number_function("1233"))
print(is_number_function("12334df.13.dff"))
