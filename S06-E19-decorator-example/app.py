# username -password -blocklist
from functools import wraps

user_list = {
    "ali123": "345678",
    "sahand": "1643",
    "mina": "0987"
}
black_list = {"mina", "sahand"}


def block_function(func):
    @wraps(func)
    def inner(*args, **kwargs):
        # print(args[0] in black_list)
        if args[0] in black_list:
            print("blocccckked")
        else:
            func(*args, **kwargs)

    return inner


@block_function
def user_show(user_name):
    print(user_name, user_list[user_name])


user_show("sahand")


@block_function
def change_password(username, newpassword):
    user_list[username] = newpassword
    print(username, user_list[username])


change_password("ali123", "bddfdv")
print("*" * 50, "\tnew exp :")
# runtime
from time import perf_counter


def time_function(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        finish_time = perf_counter()
        run_time = finish_time - start_time
        print(run_time)

    return inner


@time_function
def function(x):
    sum = 0
    for i in range(x):
        sum += i ** 2


function(1000)
