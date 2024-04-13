name = "melika Karimi"
x = 2
y = 2.4567789
# .format
print("x is : {}\n and\ny is : {}".format(4, y, 5 + 2))
print("---")
# شماره گذاری برای متغیر ها
print("x is : {2}\nand\ny is : {0}".format(4, y, 5 + 2))
print("---")
print("x is : {0}\nand\ny is : {0}".format(4, y, 5 + 2))
# using dictionary => علامت ** یادت نره
x = {"x": 2, "y": 2.34545}
print("x is {x} \nand\ny is {y}".format(**x))
print("---")
print("x is {y} \nand\ny is {x}".format(**x))
# توالی در چاپ : * یادت نره
print("x is {1}\ny is {4}".format(*"Melika"))

# "{" [field_name] ["!"conversion] [":"format_spec] "}"
# field_format
print("x is {0}".format(5))
# "!"conversion => type of variable
print("x is {0!s}".format(5))
# ":"format_spec
print("x is {:.2}".format((3.23344)))
print("x is {:.2}".format((3.23344)))
# # :[[fill]align][sign][#][0][width][grouping-option][.precision][type]
# # type : تایپ ها را از داکیومنت چک میکنیم
print("x is {0:b}".format((3546)))
print("x is {:c}".format((56)))
#  % : درصد را نمایش میدهد
print("x is {:%}".format((.45)))
print("x is {:s}".format(("melika")))
# .precision
print("x is {:.2f}".format((123.5345466)))
# grouping-option => جدا کردن سه تا سه تایی اعداد از هم
print("x is {:,.4f}".format((1223446535436.56)))
print("x is {:_.4f}".format((1223446535436.56)))
# width
print("x is {:22_.4f}".format((1223446535436.56)))
print("x is {:32_.4f}".format((1223446535436.56)))
# 0
print("x is {:032_.4f}".format((1223446535436.56)))  # با 0 پر میکند
# # : برای مبناها
print("x is {:#b}".format(43))
print("x is {:#o}".format(43))
print("x is {:#x}".format(43))
# sign => + - or space
print("x is {:+}".format(43))
print("x is {:-}".format(43))
print("x is {: }".format(43))  # space
print("x is {: }".format(-43))
# [fill]align => پر کردن فضاهای خالی و مشخص کردن جهت آنها
# # algin
print("x is {:<14}".format(43), "*")
print("x is {:>14}".format(43), "*")
print("x is {:^14}".format(43), "*")
print("x is {:^14}".format(43), "*")
# # fill
print("x is {:q^14}".format(43), "*")

# مشخص کردن موارد توسط کاربر
print("x is {:{fill}^14}".format(43, fill="g"), "*")
