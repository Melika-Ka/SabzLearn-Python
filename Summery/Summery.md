### link

- [link_1](https://github.com/MHBehroozi/pythonlearning)
- [link_2](https://github.com/rezadolati01/pamphlets)

---

---

---

# S00

## S00-E09-py-paradigm

- paradigm : الگو، شیوه و روش برنامه نویسی
- یک زبان میتواند چندین پارادایم را پشتیبانی کند
- paradigm
    1. Imperative دستوری
        - Procedual Programming برنامه نویسی پروسه ای
        - Object Oriented Programing (OOP)برنامه نویسی شی گرا
        - Parallel Processing رایانش موازی
    2. Declarative
        - Logical Programming برنامه نویسی منطقی
        - Functional Programming برنامه نویسی تابعی
        - Database Programming برنامه نویسی پایگاه داده

## S00-E10-py-what-is-python

## S00-E14-py-algorithm-part1.mp4

- algorithm :

1. ورودی
2. خروجی
3. قطعیت
4. محدودیت

# S01

## S01-E01-py-environments

- مفسر و IDLE
- خط فرمان و ترمینال
- notepad
- IDE => integrated development enviroment
- code editor like vscode
- nootebook like jopiter
- web

## S01-E06-py-jupyter

- command : `pip install ipython`
- [jupyter](https://jupyter.org/)
- [anaconda](https://www.anaconda.com/)

## S01-E08-py-web

- searching : python online interpreter

## S01-E10-pycharm-env-part2

- ctrl + f => search
- ctrl + r => search
- ctrl + shift + arrow key => move or select
- alt => select many lines
- ctrl + alt + l => مرتب کردن کد ها
- ctrl + w => انتخاب کد ها به سمت بالا
- ctrl + d => کپی یک خط به سمت پایین
- ctrl + / => comment

## S01-E11-pycharm-env-part3

- ctrl + space => پیشگویی
- alt + Enter => import library of method
- ctrl + alt + o => delete unnecessary library
- view => quick definition || ctrl + shift + i => توضیح متد ها
- view => quick documentation || ctrl + q => داکیومنت
- view => نکات مهم
- code => folding => fold => بسته و باز کردن کد ها
- ctrl + ~ => دسترسی های سریع
- ctrl + shift + a => actions
- select method => ctrl + b => توضیحات
- shift + Enter => رفتن به خط بعد در هرجا از کد
- ctrl + shift + z # ctrl + z
- ctrl + arrow key => جا به جایی بین کلمات و صفحه

# S02

## S02-E01-py-syntax-and-rows

- syntax : how to code
- rows

    1. physical lines => ما میبینیم
    2. logical lines => مفسر میبینه

    - use `;` end the lines
    - #PEP => راهنما برای تمیزی کد

## S02-E02-py-comment-docstring

- comment => # (number sign)
    - کسی که کد های منو توسعه بده
- docstring => ابتدای یک تابع یا کلاس برای توضیح ان تابع یا کلاس
    - کسی که از متد یا تابع من استفاده میکنه

```py
# this is a comment
def my_function():
    """to print hello - this is a docstring"""
    print("hello")
```

## S02-E03-py-indentation

- plugin : indent rainbow

## S02-E04-py-input-output

- input => process => output

- separator

```python
x = 2
y = 4
print("square is :", x * y, sep="-")
```

- end

```python
print("end", end="-")
```

- input

```python
name = input("Enter your name :")
print(name)
```

## S02-E05-py-variable

- variable
    - print variable address

```python
a = 1
print('a = 1 : ', id(a))
a = 2
print('a = 2 : ', id(a))
b = 2
print('b = 2 : ', id(a))

# a = 1 & a = 2 & b =2 have same address
```

- exchange two variable

```python
c, d, e, f = 5, 5, 6, 11
# exchange c & f
c, f = f, c
print('exchange c & f  =>  ', "c : ", c, " &  f : ", f)
```

delete variable

```python
m = 1
del m
```

## S02-E06-identifier

- شناسه
    - variable : `_` or `a-z` or `A-Z`

```python
# variable
a = 8
A = "Ali"
# شناسه خصوصی
_a = 2.3
#  شناسه خصوصی کلاس ها
__a = 1


# class
class MyClass:
    pass


# function
## to print docstring
def print_doc():
    """this is docstring"""
    pass


print(print_doc.__doc__)
```

- class name : is better to write PascalCase
- function name : is better to write small(or camelCase) and use\_ between each word
- variable name : is better to write small
- plugin : string manipulation

## S02-E07-keywords

```python
import keyword

help("keywords")

#
key = keyword.iskeyword("def")
print(key)  # return True or False

#
keyList = keyword.kwlist
print(keyList)

# length of array
print(len(keyList))
```

## S02-E08-arithmetic-operators

- addition : `+`
- subtraction : `-`
- multiplication : `*`
- division : `/`
- modulus : `%`
- exponentiation : `**`
- floor division : `//`

```python
x = 5
y = 4
z = x + y
print("+", z)

z = x - y
print("-", z)

z = x * y
print("*", z)

z = x / y
print("/", z)

z = x % y
print("%", z)

z = x ** y
print("**", z)

z = x // y
print("//", z)
```

## S02-E09-comparison-operators

- equal : `==`
- not equal : `!=`
- greater than : `>`
- less than : `<`
- greater than or equal to : `>=`
- less than or equal to : `<=`
- return True Or False

## S02-E10-assignment-operators

- `=` : `x = 5`
- `+=` : `x += 5` : `x = x + 5`
- `-=` : `x -= 3` : `x = x - 3`
- `*=` : `x *= 3` : `x = x * 3`
- `/=` : `x /= 3` : `x = x / 3`
- `%=` : `x %= 3` : `x = x % 3`
- `//=` : `x //= 3` : `x = x // 3`
- `**=` : `x **= 3` : `x = x ** 3`
- binary operator :
- `&=` : `x &= 3` : `x = x & 3`
- `|=` : `x |= 3` : `x = x | 3`
- `^=` : `x ^= 3` : `x = x ^ 3`
- `>>=` : `x >>= 3` : `x = x >> 3`
- `<<=` : `x <<= 3` : `x = x << 3`

*** CODE IN PYTHON FILE

## S02-E11-logical-operators

- and : returns true if both statements are true
- or :  returns false if both statements are false
- not : reverse thr result

```python
x = 5
y = 3
print(x < 4 or y < 4)  # return True
print(x < 4 and y < 4)  # return False
print(not (x < 6))  # returns False
print(not False)
```

## S02-E12-membership-operators

- in
- not in

```python
# x in y   => y میتواند رشته باشد یا ارایه باشد 
s = "Melika karimi"
print("m" in s)  # returns True
print("m" not in s)  # returns False
my_list = [1, 2, 3, 4]
print(5 in my_list)  # returns False
```

## S02-E13-identity-operators

- identity-operators => عملگر های هویت
- is : returns true if both variable are the same object
    - باید خانه حافظه یکسان داشته باشند
- is not : returns true if both variable are not the same object

```python
x = 5
y = 5
z = 4
print(x is y)  # returns True
print(x is not z)  # returns True

# list 
a = [1, 2, 3]
b = [1, 2, 3]
print("a==b ? : ", a == b)  # returns True 
print("a is b : ", a is b)  # returns False
print("id(a) : ", id(a))
print("id(b) : ", id(b))

# 
c = a
print("id(c) : ", id(c))
print("a==c ? : ", a == c)  # returns True
print("a is c ? : ", a is c)  # returns True

```

## S02-E14-bitwise-operators

- `&` : And => set each bit to 1 if both bits are 1
- `|` : Or => set each bit to 1 if one of two bits is 1
- `^` : Xor => set each bit to 1 if only one of two bits is 1
- `~` : Not => invert all the bits
- `<<` : Zero fill left shift
- `>>` : signed right shift

```python
x = 0b10101
print(x)
```

*** CODE IN PYTHON FILE

## S02-E15-walrus

```python
x = 2
# print(x=3)  # it does not work
print(x := 3)  # it does work
```

## S02-E16-operator-precedence

## S02-E17-expressions-and-statements

- expressions : تولید یک مقدار و قابل ارزیابی
- statement :  دستوری : انجام یک دستور
    - دستورات ساده : x = 7
    - دستورات مرکب یک بخشی: مثل توابع
    - دستورات مرکب چند بخشی : مثل شرط ها
    - میتوانند چیزی را هم تولید نکنند
    - از عبارت ها تولید میشود

## S02-E18-class-method-attribute

- object oriented programming => OOP

## S02-E19-pep8-pep20