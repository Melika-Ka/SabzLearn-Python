set1 = {1, 3, 4, 6, 8}
set1.add(5)
print(set1)
# موارد تکراری را قبول نمیکنند
set1.add(4)
print(set1)

# tuple are immutable
t = (1, 2)
print(id(t))  # 1
t += (5,)
print(id(t))  # 2
print(t)
# 1 & 2 have different id

# set
print(id(set1))  # 1
set1.add(10)
print(id(set1))  # 2
# 1 & 2 have  id
# ---
# اکولاد خالی
s = {}
print(type(s))
# درست کردن ست خالی
s = set()
print(type(s))
set2 = set([1, 2, 3, 4])
print(set2)
set3 = set("Melika")
print(set3)
# update
set3.update([1, 2, 3])
print(set3)
# remove
# set3.remove(5)  # error
set3.remove(3)
print(set3)
# discard
set3.discard(6)
print(set3)
# اشتراک - اجتماع و ..
p = {3, 9, 15, 12, 6, 18}
q = {12, 18, 6, 10, 4, 16, 2, 8, 14}
# منها
print(p - q)
print(p.difference(q))
# اجتماع
print(p | q)
print(p.union(q))
# اشتراک
print(p & q)
print(p.intersection(q))
# تفاضل متقابل
print(p ^ q)
print(p.symmetric_difference(q))
# زیر مجموعه بودن یا نبودن
p = {40, 50, 20, 10, 30, 60}
q = {10, 30, 60}
# زیر مجموعه بودن
print(p < q)
print(p.issubset(q))
# ابر مجموعه بودن
print(p > q)
print(p.issuperset(q))