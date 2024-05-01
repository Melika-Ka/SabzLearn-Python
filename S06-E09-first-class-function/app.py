## 1
def function1(x):
    print(x * 2)


x = 5
y = function1
y(x)

## 2

x = True
if x:
    def function2():
        print(x ** 2)
function2()


## 3
def A(a):
    print(a)

    def B(b):
        print(b ** 2)

    B(a)


A(5)
print(A.__name__)


# print(B)  # not defined in dom

## 4

# def descending(myList):
#     print(sorted(myList, reverse=True))
#
#
# def ascending(myList):
#     print(sorted(myList))
#
#
# def mysort(function, myList):
#     return function(myList)
#
#
# mysort(descending, [1234, 342, 456563, 7, 4, 4, 35, 4657, 68, 4, 5, 6])
# mysort(ascending, [1234, 342, 456563, 7, 4, 4, 35, 4657, 68, 4, 5, 6])


## 5
def mysort(s):
    def descending(myList):
        print(sorted(myList, reverse=True))

    def ascending(myList):
        print(sorted(myList))

    def error(myList):
        print("Error!! your list : \n", myList)

    if s == "a":
        return ascending
    elif s == "d":
        return descending
    else:
        return error


user_input = input("Enter your choice")
answer = mysort(user_input)
answer([1234, 342, 456563, 7, 4, 4, 35, 4657, 68, 4, 5, 6])
