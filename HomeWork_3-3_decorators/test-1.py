def speed(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Your function execution time is {end - start}')

    return wrapper()


@speed
def sorting():
    from random import randint
    a = (randint(1, 30000000) for _ in range(1000000))
    b = sorted(a)
    return b

# print(type(sorting()))
sorting()
