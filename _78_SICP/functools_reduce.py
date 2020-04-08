import functools
import operator

a = '23215232'
a = [int(i) for i in a]

ttl = functools.reduce(operator.mul, a)
assert ttl == 720
