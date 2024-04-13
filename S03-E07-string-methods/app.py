name = "melika karimi"
# len() => طول رشته
string_len = len(name)
print("string_len : ", string_len)
print("name[4:len(name)] : ", name[4:len(name)])
# .upper() => تبدیل حروف رشته به حروف بزرگ
string_upper = name.upper()
print("string_upper : ", string_upper)
# .lower() => تبدیل حروف رشته به حرف کوچک
string_lower = name.lower()
print("string_lower : ", string_lower)
# .count() => شمارش یک یا چند حرف خاص در یک رشته
string_count = name.count("m")
print("string_count (m) : ", string_count)
# .endswith() => ایا رشته من با کاراکتر خاصی پایان یافته است یا نه
string_endswith = name.endswith("a")
print("string_endswith (a) : ", string_endswith)
# .startswith()
string_startswith = name.startswith("m")
print("string_startswith (m) : ", string_startswith)
# .find() => پیدا کردن یک کاراکتر خاص در رشته از سمت چپ
string_find = name.find("k")
print("string_find (k) : ", string_find)
# .rfind() => پیدا کردن یک کاراکتر خاص در رشته از سمت راست
string_rfind = name.rfind("k")
print("string_rfind (k) : ", string_rfind)
# .isalnum() => ایا تمام این کاراکتر ها از حرف و عدد هستند یا خیر
name_1 = "melika"
string_isalnum = name_1.isalnum()
print("string_isalnum : ", string_isalnum)
# .isnumeric() => فقط و فقط از ارقام است یا نه
string_isnumeric = name.isnumeric()
print("string_isnumeric : ", string_isnumeric)
# .join() => چسباندن یک لیست شامل
star = "*"
lst = ["A", "B", "C"]
string_join = star.join(lst)
print("string_join : ", string_join)
# .split() => جدا کردن رشته ها برحسب یک کارکتر خاص و قرار داند آنها در یک لیست
s = "Melika,Karimi,Tehran"
string_split = s.split(",")
print("string_split : ", string_split)
# .replace("old","new") => جایگذاری کارکتری با یک کاراکتر دیگر
string_replace = name.replace("m", "n")
print("string_replace : ", string_replace)
# .strip() => حذف تعدادی کاراکتر از اول یا اخر رشته
string_strip = name.strip()  # حذف فاصله
print("string_strip : ", string_strip)
name_1 = "++++MELIKA+++"
string_strip_2 = name_1.strip("+")
print("string_strip_+ : ", string_strip_2)
# .rstrip() => حذف تعدادی کاراکتر از سمت راست رشته
name_1 = "++++MELIKA+++"
string_rstrip = name_1.rstrip("+")
print("string_rstrip : ", string_rstrip)
# .lstrip() => حذف تعدادی کاراکتر از سمت چپ رشته
name_1 = "++++MELIKA+++"
string_lstrip = name_1.lstrip("+")
print("string_lstrip : ", string_lstrip)
# .capitalize() => اولین کاکراکتر را حتبدیل به حرف بزرگ میکند
string_capitalize = name.capitalize()
print("string_capitalize : ", string_capitalize)


