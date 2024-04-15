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

> CODE IN PYTHON FILE

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
# x in y => y میتواند رشته باشد یا ارایه باشد 
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

> CODE IN PYTHON FILE

## S02-E15-walrus

```python
x = 2
# print(x=3)  # it does not work
print(x := 3)  # it does work
```

## S02-E16-operator-precedence

## S02-E17-expressions-and-statements

- expressions : تولید یک مقدار و قابل ارزیابی
- statement : دستوری : انجام یک دستور
    - دستورات ساده : x = 7
    - دستورات مرکب یک بخشی: مثل توابع
    - دستورات مرکب چند بخشی : مثل شرط ها
    - میتوانند چیزی را هم تولید نکنند
    - از عبارت ها تولید میشود

## S02-E18-class-method-attribute

- object oriented programming => OOP

## S02-E19-pep8-pep20

- [peps](http://python.org/dev/peps)

- [pep20](https://peps.python.org/pep-0020/)
    - [pep20_by_example.py](https://gist.github.com/evandrix/2030615)

```python
import this  # ctrl + b
```

- [pep8](https://peps.python.org/pep-0008/)
    - [pep8_persin](https://pep8.ir/)

# S03

## S03-E01-data-types

python data type :

- numeric
    - integer
    - float
    - complex
- dictionary
- boolean
- set
- sequence type
    - string
    - list
    - tuple
- special

## S03-E02-numbers

- integer
- float
- complex

- casting => تبدیل واحد بزرگ تر به کوچک تر

> CODE IN PYTHON FILE

## S03-E03-example-for-numbers

> CODE IN PYTHON FILE

## S03-E04-exercises-season3-numbers

> CODE IN PYTHON FILE

## S03-E05-string-part1

- strings in Python are arrays of bytes representing unicode characters.
- You can assign a multiline string to a variable by using three quotes Or three single quotes
- `isinstance(variable, datatype)` => نمونه ای از یک دیتا تایپ خاصی هست یا خیر
- `type(variable)`
- `\n` => رفتن به خط بعدی
- `\` or r => لغو کاری
- `*` or duplicate => تکرار
- `+` or contact => چسباندن بهم

## S03-E06-string-part2

- index
- slice
- len => سایز رشته
- Looping Through a String :

```python
for x in "banana":
    print(x)
```

## S03-E07-string-methods

- [string methods](https://www.w3schools.com/python/python_ref_string.asp)
- function : `fync_name(string_varible)` => like :`len()`
- method : `string_variable.method_name()` => like :`upper()`

1. `len()` : سایز رشته
2. `.upper()` => تبدیل حروف رشته به حروف بزرگ (returns the string in upper case)
3. `.lower()` => تبدیل حروف رشته به حرف کوچک (returns the string in lower case)
    - `casefold()` => This method is similar to the `lower()` method, but the `casefold()` method is stronger, more
      aggressive, meaning that it will convert more characters into lower case, and will find more matches when
      comparing two strings and both are converted using the `casefold()` method.
4. `.count()` => شمارش یک یا چند حرف خاص در یک رشته
5. `.endswith()` => ایا رشته من با کاراکتر خاصی پایان یافته است یا نه(Returns true if the string ends with the specified
   value)
6. `.startswith()` => (Returns true if the string starts with the specified value)
7. `.find()` => پیدا کردن یک کاراکتر خاص در رشته از سمت چپ
8. `.rfind()` => پیدا کردن یک کاراکتر خاص در رشته از سمت راست
9. `.isalnum()` => ایا تمام این کاراکتر ها از حرف و عدد هستند یا خیر
10. `.isnumeric()` => فقط و فقط از ارقام است یا نه (    Returns True if all characters in the string are numeric)
11. `.join()` => چسباندن یک لیست شامل (Joins the elements of an iterable to the end of the string)
12. `.split()` => جدا کردن رشته ها برحسب یک کارکتر خاص و قرار داند آنها در یک لیست (returns a list where the text
    between the specified separator becomes the list items)
13. `.replace("old","new")` => جایگذاری کارکتری با یک کاراکتر دیگر (replaces a string with another string)
14. `.strip()` => حذف تعدادی کاراکتر از اول یا اخر رشته (removes any whitespace from the beginning or the end)
15. `.rstrip()` => حذف تعدادی کاراکتر از سمت راست رشته
16. `.lstrip()` => حذف تعدادی کاراکتر از سمت چپ رشته
17. `.capitalize()` => اولین کاکراکتر را حتبدیل به حرف بزرگ میکند
18. `in` => To check if a certain phrase or character is present in a string
19. `not in` => To check if a certain phrase or character is NOT present in a string

> CODE IN PYTHON FILE

## S03-E08-unicode-escape-characters

- start with `\`
- [ascii](https://www.asciitable.com/)
- [unicode](https://www.utf8-chartable.de/)

- [strings_escape](https://www.w3schools.com/python/python_strings_escape.asp)
- `ord()` => پیدا کردن یونیکد یک رشته یا حرف یا کاراکتر
- `char()` => پیدا کردن حروف یا کاراکتر یک یونیکد
- `\b` => حذف کردن یک کاراکتر قبلی
- `\r` => کاراکتر های بعدی را وارد خط اول میکند
- `\t` => فاصله یک تب

## S03-E09-traditional-string-format

- [string_formatting](https://www.w3schools.com/python/python_string_formatting.asp)

- `"%[(key)][flag][w][.p] type" %(مقدار یا متغیر )`

> CODE IN PYTHON FILE

## S03-E10-string-format-with-format

- [pythons document](https://docs.python.org/3/library/string.html)
- `.format()`

    - `"{" [field_name] ["!"conversion] [":"format_spec] "}"`

        - `:[[fill]align][sign][#][0][width][grouping-option][.precision][type]`

> CODE IN PYTHON FILE

## S03-E11-f-string

- f string => python 3.6
- module : `import datetime`
    - [datetime in python documents](https://docs.python.org/3/library/datetime.html)

> CODE IN PYTHON FILE

## S03-E12-example-for-string

## S03-E13-exercises-season3-strings

- `.isdecimal()` = `.isdigit()` = `.isnumeric()`