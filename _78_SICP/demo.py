def rang(age):
    """ 17<age<=65"""
    return max(min(65, age), 17)

print(rang(99))
