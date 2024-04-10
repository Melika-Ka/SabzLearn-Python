# برنامه ای که وزن را به کیلوگرم دریافت کند و به صورت گرم نشان دهد
user_input_kg = input("enter number (kg)")
print("type(user_input_kg) :", type(user_input_kg))
# print(user_input_kg * 10)
user_input_kg_number = int(user_input_kg)
kg_to_gr = user_input_kg_number * 1e+3
print("kg_to_gr : ", kg_to_gr, " gr")

# ---------------------------------
# مساحت یک مثلت را حساب کنید
h = input("h : ")
b = input("b : ")
h, b = int(h), int(b)
s = h * b / 2
print("S : ", s)

# --------------------------------
# ماشین حساب بسیار ساده

# -------------------------------
# یک عدد از کاربر بگیریم و ارقام ان را جدا کنیم
x = int(input("Enter x (3 digits) : "))
print(x % 10)
x //= 10
print(x % 10)
x //= 10
print(x % 10)

# ---------------------------
# تبدیل درجه به رادیان
