# تعداد تکرار یک کاراکتر
# text = "Hello world ! I`m a developer"
# user_input = input("Enter Your char")
# print(text.count(user_input))
# ------
# اخرین کلمه یک متن
# user_txt = input("Enter your text").rstrip()
# last_space_index = user_txt.rfind(" ")
# print(last_space_index)
# print(user_txt[last_space_index+1:])
# ------
# ایا جمله دوم در جمله اول هست یا نه
# txt_1 = input("Enter Txt 1")
# txt_2 = input("Enter Txt 2")
# print(txt_2 in txt_1)
# ------
# پاک کردن تمام اسپسش ها و فاصله ها
# text = input("Enter your text")
# print(text.replace(" ", "").replace("\t", ""))
# حذف عدد صفر از سمت چپ شماره
user_phone = input("Enter your phone number")
print(user_phone.lstrip("0"))
