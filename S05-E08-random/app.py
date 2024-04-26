from random import choice, randint

# from random import random, randint, uniform, randrange, choice , sample , shuffle
# for _ in range(100):
#     print(random())
#     print(20 * "..")
#     print(randint(2, 5))
#     print(20 * "..")
#     print(uniform(2, 5))
#     print(20 * "..")
#     print(randrange(2, 100, 2))
####
x = ["a", "b", "c", "d", "e", "f", "h", "i", "j", "k", "l", "n", "m"]
# for _ in range(10):
#     # print(x[randint(0, len(x) - 1)])
#     print(choice(x))
# print(sample(x, 4))
# y = x.copy()
# shuffle(y)
# print(y)
## شیر خط
coin = ["tails", "heads"]
tail = 0
head = 0
for _ in range(1000):
    rand = choice(coin)
    if rand == "tails":
        tail += 1
    else:
        head += 1
print("tails : ", tail, "heads : ", head)

# تاس
tas = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}
for _ in range(1000):
    x = randint(1, 6)
    tas[x] += 1
print(tas)
