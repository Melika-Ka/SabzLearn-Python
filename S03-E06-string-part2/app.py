name = "abcdef"
family = "ghijklmn"
# indexing
print(name[0])
print(family[-1])
# print(name[12])  # => error
# name[2] = "m" # => error
# slicing
print(name[2:5])
print(family[0:-2])
print(family[-1:-2])  # not correct
print(family[-2:-1])  # correct
print(family[:-3])  # از اول
print(family[-3:])  # تا اخر
print(name[:3] + name[3:])
print(name[12:13])  # it works
# مشخص کردن گام
print(family[0:5:2])  # گام دو
print(name[::2])
print(name[::-2])  # گام دو از اخر به اول
# سایز رشته
print(len(name))
