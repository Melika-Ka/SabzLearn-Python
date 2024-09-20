import statistics


def medians(*a):
    lst = []
    for i in a:
        lst.append(i)
    print(statistics.median(lst))


def average(*a):
    sum = 0
    len = 0
    for i in a:
        sum += i
        len += 1
    print(sum / len)


def variance(*a):
    lst = []
    for i in a:
        lst.append(i)
    print(statistics.variance(lst))
