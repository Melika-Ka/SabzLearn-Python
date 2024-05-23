# 1
# def san_gn(san_list):
#     w = None
#     while True:
#         name = yield w
#         if name not in san_list:
#             w = name
#         else:
#             w = "*" * len(name)
#
#
# result = san_gn(["khar", "gov"])
# result.__next__()
# print(result.send("khar"))
# print(result.send("melika"))
# print(result.send("gov"))
# print(result.send("sahel"))
# print(result.send("khar"))

# 2
def split_gn(split_mark=""):
    split_result = None
    while True:
        split_list = yield split_result
        split_result = split_list.split(split_mark)


result = split_gn(",")
next(result)
print(result.send("m,df,hg,h,fd"))
