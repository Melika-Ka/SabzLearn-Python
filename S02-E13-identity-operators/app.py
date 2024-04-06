x = 5
y = 5
z = 4
print("x is y ?: ", x is y)  # returns True
print("x is not z ?: ", x is not z)  # returns True

#
w = x
print("id(x)", id(x))
print("id(w)", id(w))
print("id(y)", id(y))

#
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
