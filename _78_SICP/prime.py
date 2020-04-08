
def is_prime(n):
    def smallest_divisor(n):
        return find_divisor(n, 2)
    def find_divisor(n, test_divisor):
        if square(test_divisor)>n:
            return n
        if is_divides(test_divisor, n):
            return test_divisor
        return find_divisor(n, test_divisor+1)
    def is_divides(a, b):
        return (b%a)==0
    def square(a):
        return a*a

    return smallest_divisor(n) == n

if __name__ == '__main__':
    li = [11, 21, 49, 61, 73, 111, 10_000_000_000]
    for i in li:
        print(is_prime(i))
