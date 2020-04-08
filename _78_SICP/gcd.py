def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

assert gcd(16, 28) == 4
assert gcd(206, 40) == 2

