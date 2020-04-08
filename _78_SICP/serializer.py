"""
==========================================================================================
v0, @ZL. create a tangibale example to display how to implement the concept of serializer

==========================================================================================
"""

def add(a, b):
    """linear recursive proc"""
    if a == 0:
        return b
    return add(a-1, b+1)

def sub(a, b):
    """linear recursive proc"""
    if b == 0:
        return a
    return sub(a-1, b-1)

def mul2(a, b):
    """linear recursive"""
    if b == 1:
        return a
    return a + mul(a, b-1)

def mul(a, b):
    return a * b

if __name__ == '__main__':
    import concurrent.futures

    funcs = [add, sub, mul]

    global a
    global b
    a, b = 2, 3

    #concurrent proc
    print("concurrent proc")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for func in funcs:
            a = executor.submit(func, a, b).result()
            b = a + 1
            print(func.__name__)
            print("    a:{:>4}, b:{:>4}".format(a,b))

    #non concurrent proc
    a, b = 2, 3
    print("\nnon concurrent proc")
    for func in funcs:
        a = func(a, b)
        b = a + 1
        print(func.__name__)
        print("    a:{:>4}, b:{:>4}".format(a,b))
