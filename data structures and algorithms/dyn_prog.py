# 2169435 -> 525
def rec(num, result):
    num = str(num)
    result = str(result)
    num2 = int(num[:len(num)])
    flag1 = len(num) < len(result)
    flag2 = int(result) - int(num[len(num):])
    if flag1 and flag2 > 0:
        return rec(num2, flag2)


def dyn_prog(num, result):
    num = str(num)
    result = str(result)
    flag1 = 1
    flag2 = 1
    while flag1 and flag2 > 0:
        num2 = int(num[:len(num)])
        result2 = flag2
        return rec(num, result)


