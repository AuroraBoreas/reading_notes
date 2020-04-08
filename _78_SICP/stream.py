
import functools

@functools.lru_cache(maxsize=64, typed=False)
def fib(num):
    l = [0, 1]
    if num > 2:
        for i in range(num-2):
            r = l[-1] + l[-2]
            l.append(r)
    return l

if __name__ == '__main__':
    f = fib(200)
    print(f)
