import decimal

# binary
import fractions

x = 0b1101
print(x)
print(type(x))
# octal
z = 0o342
print(z)
print(type(z))
# hexadecimal
y = 0xAB
print(y)
print(type(y))

# decimal
dec = 14
print(bin(dec))
print(oct(dec))
print(hex(dec))

# int to float
int_to_float = 1
print(float(int_to_float))
# float to int
float_to_int = 1.9
print(int(float_to_int))
# int to complex
int_to_complex = 1
print(complex(int_to_complex))
#  complex to int => not works
# complex_to_int = 1 + 2j
# print(int(complex_to_int))
# special string to int
str_not_to_int = "baby"
str_to_int = "12"
print(int(str_to_int))
# int to str
int_to_str = 12
print(str(int_to_str))
#
f = 0.1 + 0.2
print(f)  # چون به شکل باینری ذخیره میشود
print(f == 0.3)  # return false
# راه حل

# from decimal import Decimal
# حتما به صورت رشته باشند
decimal_Decimal = decimal.Decimal("0.1") + decimal.Decimal("0.2")
print(decimal_Decimal)
print(type(decimal_Decimal))

#
# fractions => اعداد کسری
fraction = fractions.Fraction(1.5)
print(fraction)

# خوانایی اعداد بزرگ
x = 1_000_000_000
print(x)
# exponential
f = 1e+7
f = 1e-7
print(f)

# inf
x = 2e+300
x = 2e+400
print(x)
print(type(x))

# complex
z = 3 + 2j
print(z.real)
print(z.imag)
print(z.conjugate())  # مزدوج
# round
c = 3.23456
print(round(c, 4))
 