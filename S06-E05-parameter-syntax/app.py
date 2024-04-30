# normal
def func(a, b, c, d):
    print("a : ", a)
    print("b : ", b)
    print("c : ", c)
    print("d : ", d)


# default value
def func2(a=3, b=6, c=8, d=9):
    print("a : ", a)
    print("b : ", b)
    print("c : ", c)
    print("d : ", d)


func2()
print(30 * "-")
func2(2, 4, 5)
print(30 * "-")
func2(c=4)


# normal + default value
def func3(a, b, c=8, d=9):
    print("a : ", a)
    print("b : ", b)
    print("c : ", c)
    print("d : ", d)


print(30 * "-")
func3(3, 2, d=6)


# *name
def func4(a, b, c, *d):
    print("a : ", a)
    print("b : ", b)
    print("c : ", c)
    print("d : ", d)


print(30 * "-")
func4(2, 4, 6, 6, 7, 8, 98, 990)
print(30 * "-")
func4(1, 2, 3)  # d=()


# *name => غیر اخری

def func5(a, b, *c, d):
    print("a : ", a)
    print("b : ", b)
    print("c : ", c)
    print("d : ", d)


print(30 * "-")
func5(2, 4, 6, 6, 7, 8, 98, d=990)


# **dict
def func6(**a):
    print(a)


print(30 * "-")
func6(a=2, c=4, d=1)


def func7(b, **a):
    print(b)
    print(a)


print(30 * "-")
func7(a=5, b=2, c=4, d=1)
print(30 * "-")
func7(10, a=2, c=4, d=1)


def func8(c, *d, **a):
    print(c)
    print(d)
    print(a)


print(30 * "-")
func8(1, 3, 345, 67, 8, 899, 8, a=4, b=5, f=6)
