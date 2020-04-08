def fact(n, current_fact=1):
    if n == 1:
        return current_fact
    else:
        return fact(n-1, current_fact*n)

print(fact(4, 1))
