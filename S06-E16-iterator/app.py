print(dir([1, 2, 3]))  # متدهای یک ارایه
print("__iter__" in dir(5))
print("__iter__" in dir("Melika"))
print("__iter__" in dir(range(10)))

###
i = [1, 2, 3, 4]
# print(next(i))   # error
print("__next__" in dir(i))
i = iter(i)
# i = i.__iter__()
print("__next__" in dir(i))
print(next(i))
print(i.__next__())
print(next(i))
print(next(i))
# print(next(i))  # error in the end of the arrray

##
p = [1, 2, 3, 5, 79, 0]
p = iter(p)
while True:
    try:
        print(next(p))
    except StopIteration:
        break

##

from itertools import count

print(dir(count))
print("__next__" in dir(count))
counter = count()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
counter = count(10)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
