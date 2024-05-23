# # 1
# def func():
#     """this is doc"""
#     pass
#
#
# print(dir(func))
# print(func.__doc__)
# print(func.__name__)

# 2
def avg_1(li):
    return sum(li) / len(li)


def avg_2(li):
    return sum(li) / len(li)


avg_1.school_name = "school_1"
# avg_2.school_name = "school_2"
setattr(avg_2, "school_name", "school_2")
print(avg_1.school_name)
# print(dir(avg_2))
print(avg_2.__dict__)
print(getattr(avg_1, "school_name"))

if hasattr(avg_2, "school_name"):
    print(getattr(avg_2, "school_name"))

# delattr(avg_1, "school_name")
del avg_1.school_name
print(avg_1.__dict__)
