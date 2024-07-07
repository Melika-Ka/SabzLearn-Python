# 1
# normal
print("normal")
s = []
for i in range(10):
    s.append(i ** 2)
print(s)

# comprehension
print("comprehension")
x = [i ** 2 for i in range(10)]
print(x)
print("--" * 20)

# 2
# comprehension
print("comprehension")
z = [i for i in range(10) for j in range(10) if i > 8]
print(z)
print("--" * 20)

# 3
# normal
print("normal")
m = list(map(lambda i: i ** 2, range(10)))
print(m)

# comprehension
print("comprehension")
m = [i ** 2 for i in range(10)]
print(m)
print("--" * 20)

# 4
# normal
print("normal")
s = []
for i in range(10):
    if i % 2 == 0:
        s.append(i)
print(s)

# comprehension
print("comprehension")
s = [i for i in range(10) if i % 2 == 0]
print(s)
print("--" * 20)

# 5
# normal
print("normal : ")
s1 = [1, 2, 3]
s2 = [4, 2, 6]
s = []
for i in s1:
    for j in s2:
        if i != j:
            s.append((i, j))
print(s)
# comprehension
print("comprehension : ")
s = [(i, j) for i in s1 for j in s2 if i != j]
print(s)
print("--" * 20)

# 6
# comprehension
print("comprehension")
z = [-1, 2, -4, 5, -7, 7, -10, 11, -23, 32]
x = [n ** 2 for n in z if n > 3]
x = [n ** 2 for n in z if abs(n) > 3]
print(x)
print("--" * 20)

# 7
# comprehension
print("comprehension : ")
lst = ["melika", "amir", "sara", "nilo", "jafar"]
s = [char for name in lst for char in name]
s = [char.upper() + "+" for name in lst for char in name]

print(s)
print("--" * 20)

# 8
from math import pi

# normal
print("normal")
s = []
for i in range(10):
    s.append(str(round(pi, i)))
print(s)
# comprehension
print("comprehension : ")
s = [str(round(pi, i)) for i in range(10)]
print(s)
print("--" * 20)

# 9
# normal
print("normal :")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(matrix[1][2])
print(len(matrix))
t = []
for i in range(len(matrix) + 1):
    t_row = []
    for row in matrix:
        t_row.append(row[i])
    t.append(t_row)
for j in t:
    print(j)

# comprehension
print("comprehension : ")
t = [[row[i] for row in matrix] for i in range(len(matrix) + 1)]
for j in t:
    print(j)

# zip
print("zip : ")
t = list(zip(*matrix))
t = list(zip(matrix[0], matrix[1], matrix[2]))
for j in t:
    print(j)

print("--" * 20)

# 10
x = "a"
c = [x for x in range(10)]
print(x)
print("--" * 20)

# 11
c = [x for x in (1, 2, 3)]
print(c)
print("--" * 20)
# 12 tuple
t = (1, 2, 3, 4)
c = list(t)
print(c)
print("--" * 20)
# 13 set
s = {i for i in range(10) if i % 2 != 0}
print(s)
print("--" * 20)
# 14 set
x = "sdfgf;lfd,l;'sd'g,b,'xc"
s = {i for i in x}
print(s)
print("--" * 20)

# 15 dict
x = {"reza": 25, "ali": 21, "hani": 11}
s = {key: value for key, value in x.items()}
print(s)
print("--" * 20)

# 16 dict
d1 = ["a", "b", "c"]
d2 = [12, 34, 54]
s = {key: value for key, value in zip(d1, d2)}
print(s)
print("--" * 20)

# 17 if else
x = [1, 2, 3, 4, 5, 6, 7, 8]
z = []
for i in x:
    if i % 2 == 0:
        z.append(i)
    else:
        z.append(0)
z = [i if i % 2 == 0 else 0 for i in x]
print("--" * 20)


# 18 function
def func(x):
    if x % 2 == 0:
        return x
    else:
        return 0


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
z = [func(z) for z in x]
print(z)
print("--" * 20)

# 19 function and random
from random import randrange


def func():
    return randrange(50, 150)


x = [func() for _ in range(10)]

print(x)
print("--" * 20)

# 20
# normal :
print("normal")
x = []
for i in range(10):
    if (n := func()) > 100:
        x.append(n)

# comprehension
print("comprehension : ")
x = [n for _ in range(10) if (n := func()) > 100]
print(x)
print("--" * 20)

# 21
names = ["reza", "melika", "ali"]
d = {name: [i for i in range(5)] for name in names}
print(d)
print("--" * 20)
