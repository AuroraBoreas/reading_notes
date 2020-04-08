
def sum1(a, b):
    """iteractive process"""
    print("sum1({},{})".format(a, b))
    if a==0:
        return b
    else:
        return sum1(a-1, b+1)

x = sum1(3, 4)
print(x)

def sum2(a, b):
    """recursive process"""
    print("1 + sum({},{})".format(a, b))
    if a==0:
        return b
    else:
        return 1 + sum2(a-1, b)

print()
x = sum2(3, 4)
print(x)

def factorial(n):
    def fact_iter(product, counter, max_count):
        if counter > max_count:
            return product
        return fact_iter(product*counter, counter+1, max_count)
    return fact_iter(1, 1, n)

print()
x = factorial(6)
print(x)
