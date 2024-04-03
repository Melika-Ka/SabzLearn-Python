# part1
a = 1
print('a = 1 : ', id(a))
a = 2
print('a = 2 : ', id(a))
b = 2
print('b = 2 : ', id(b))
print('a=2 & b =2 have same address')

# part2


c, d, e, f = 5, 5, 6, 11
# exchange c & f
c, f = f, c
print('exchange c & f  =>  ', "c : ", c, " &  f : ", f)

# part 3
# delete variable
m = 11
del m
