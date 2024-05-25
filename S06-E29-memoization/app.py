# سرعت بخشیدن به توابع بازگشتی
from functools import wraps


def memoized_dec(func):
    memoized = {}

    @wraps(func)
    def inner(n):
        if n not in memoized:
            memoized[n] = func(n)
        return memoized[n]

    return inner


@memoized_dec
def fibu(x):
    if x == 0 or x == 1:
        return x
    return fibu(x - 1) + fibu(x - 2)


print(fibu(300))
