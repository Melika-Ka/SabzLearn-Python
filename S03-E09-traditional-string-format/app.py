# "%[(key)][flag][w][.p] type"
# type :
# %i or %d : عدد
print("%d" % (23))
print("%i" % (23))
# %c : کاراکتر یک عدد را نشان میدهد
print("%c" % (167))
print("%c" % ("c"))
# %s : نشان دهنده رشته ها
print("%s" % ("Melika"))
# %r : نشان دهنده رشته ها
print("%r" % ("melika"))
# %o : برای تبدیل عدد به مبنای هشت
print("%o" % (12))
# %x : برای تبدیل عدد به مبنای شونزده
print("%x" % (12))
# %E : نمایش به صورت نماد علمی
print("%E" % (123455677))
# %f : اعداد اعشاری با شش رقم اعشار
print("%f" % (12.3455677))
# %a : کد اسکی را نشان میدهد
print("%a" %("§"))
# .p : تعداد رقم اعشار
print("%.4f" % (1.32445677899))
# حداقل اندازه کاراکتر
print("%24.2f" % (2.345566))
# flag :
# + : یعنی علامت ها را نشان بده
print("%+24.2f" % (2.345566))
# - : میدان را از سمت راست بچین
print("%-11.2f" % (2.566), "*")
# 0: فضاهای خالی میدان را با صفر پر میکند
print("%011.2f" % (2.566), )

# (key) : برای دیکشنری است
d = {'name': "melika", "age": 22, "city": "teh"}
print("%(name)s____%(city)r____%(age)i" % (d))
# * : وارد کردن کاربر
w = int(input("w"))
p = int(input("p number"))
print("%*.*f" % (w, p, 2.3445778))