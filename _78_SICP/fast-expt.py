import timeit

def fast_expt(b, n):
    def is_even(n):
        return n%2==0
    def square(a):
        return a*a

    if n==0:
        return 1
    if is_even(n):
        return square(fast_expt(b, n/2))
    else:
        return b*fast_expt(b, n-1)


t = min(timeit.repeat("fast_expt(5, 100)", "from __main__ import fast_expt", number=10000))
print("{}^{} = {}, {}secs".format(5, 100, fast_expt(5,100), t))
