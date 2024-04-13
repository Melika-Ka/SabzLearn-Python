x = 3
y = "melika"
name = "melika"
age = 23
# بقیه علامتا مانند حالت قبلی
print(f"x is {x}")
print(F"x is {x}")
print(F"x is {'melika'!a}")
print(F"{{x}} is {x}")
print(F"{{x}} is {{{x}}}")
# use methods
print(f"y is {y.replace('a', 'x')}")
msg = (
    f"name is {name}\n"
    f"age is {age}"
)
print(msg)

#
from datetime import datetime

today = datetime.today()
print(f"{today :%m/%b/%Y         }")

# import datetime
# print(datetime.datetime.today())
