import os
import time


def relative(relative):
    return os.path.join(os.path.dirname(__file__), relative)


def timer(func):
    def inner():
        start = time.time()
        result = func()
        finish = time.time()
        duration = (finish - start) * 1000
        print(f"{func.__name__}: {result} in {duration:,.0f}ms")
        return result

    return inner
