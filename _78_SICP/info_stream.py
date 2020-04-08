
def is_odd(n):
    if n%2 == 1:
        return True
    else:
        return False
def is_even(n):
    return False if n%2 == 1 else True

def filter(predicate, seq):
    if seq == []:
        return []
    else:
        if predicate(seq[0]):
            return [seq[0]] + filter(predicate, seq[1:])
        else:
            return filter(predicate, seq[1:])

a = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
odd_b = filter(is_odd, a)
even_b = filter(is_even, a)

print("{:+<40}".format(""))
print("original     :", a)
print("odd elements :", odd_b)
print("even elements:", even_b)
