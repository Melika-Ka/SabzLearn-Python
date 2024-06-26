lst = []
# # 1

# user_input = input("name (q is quit) : ")
# while user_input.lower() != "q":
#     lst.append(user_input)
#     user_input = input("name (q is quit) : ")

# # 2
# while True:
#     user_input = input("name (q is quit) : ")
#     if user_input.lower() == "q":
#         break
# lst.append(user_input)

# # 3
# while (user_input := input("name (q is quit) : ").lower()) != "q":
#     lst.append(user_input)
#
# print(lst)
#
a = [1, 2, 3, 4, 6, 7]
if (n := len(a)) > 3:
    print(n)
#
s = -6
print(f"{s:=10}")
print(f"{(s := 5)}")
print(f"{(s := 5):=12}")

#
a = [1, 2, 3, 4, 6, 7]

d = {
    "l": (l := len(a)),
    "s": (s := sum(a)),
    "a": l / s
}

print(d)
