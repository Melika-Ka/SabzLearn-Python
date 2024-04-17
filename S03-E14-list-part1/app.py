name_letters = list("Amin")
print(name_letters)
# ---
name = "M E L I K A"
print(name.split(" "))
# ---
my_list = [51, 23, 33, 57, 69, 43, 64]
print(my_list[0])
print(my_list[3:5])
print(my_list[::2])
# ---
print(my_list * 2)
print(my_list + [12, 65])  # تغییری در لیست اعمال نمیشود
print(my_list)

# --- mutable
my_list[1] = 55
print(my_list)
# ---
my_list_2 = [51, 55, 33, 57, 69, 43, 64]
print(my_list == my_list_2)
my_list_3 = my_list_2
print(my_list_3 == my_list_2)
#
this_list = ["apple", "banana", "cherry"]
this_list[1:2] = ["blackcurrant", "watermelon"]
print(this_list)
#
this_list = ["apple", "banana", "cherry"]
this_list[1:3] = ["watermelon"]
print(this_list)
