def mul_nums(*args):
    mul = 1
    print(args)
    for i in args:
        mul *= i
    return mul

nums = [2,3,4]
print(mul_nums(*nums))