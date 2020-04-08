def length(a):
    if a == []:
        return 0
    else:
        return 1 + length(a[1:])

def leaves(a):
    if a == []:
        return 0
    if type(a) != 'list':
        return 1
    else:
        return leaves(a[0]) + length(a[1:])


a = [[1,2],3,4]
print(length(a))
print(leaves(a))

