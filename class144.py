def mul_nums(num, *args):
    mul = 1
    for i in args:
        mul *= i
    return mul
print(mul_nums(2,3,4))
    