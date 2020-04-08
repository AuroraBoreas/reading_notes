import timeit

def expt(b, n):
    """linear recursive process"""
    if n==0:
        return 1
    return b*expt(b, n-1)

def expt2(b, n):
    """linear iteractive process"""
    def expt_iter(b, counter, product):
        if counter==0:
            return product
        return expt_iter(b, counter-1, b*product)
    return expt_iter(b, n, 1)


t = min(timeit.repeat("expt(2, 120)", "from __main__ import expt", number=10000))
print("linear recursive process takes:", t)

t = min(timeit.repeat("expt2(2, 120)", "from __main__ import expt2", number=10000))
print("linear iteractive process takes:", t)
