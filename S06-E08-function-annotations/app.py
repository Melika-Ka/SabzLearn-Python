# my py package
def function(a: int, b: int, c: int) -> list:
    return c, a


print(function(2, 3, "4"))
print(function.__annotations__)
