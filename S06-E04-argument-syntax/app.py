def maxing(a, b, c):
    print("a : ", a)
    print("b : ", b)
    print("c : ", c)
    return max(a, b, c)


# normal
print(maxing(1, 2, 3))
# name = value
print(maxing(b=4, c=2, a=3))
# normal + (name =value)
print(maxing(4, c=2, b=3))
# *iterable
print(maxing(*[1, 4, 7]))
x = {10, 9, 7}
print(maxing(*x))
# **dict
d = {"b": 4, "c": 11, "a": 56}
print(maxing(**d))
