x = 0


def A():
    nonlocal x

    # x = 2
    def B():
        # global x
        nonlocal x

        x += 1
        print(x)

    B()


A()
