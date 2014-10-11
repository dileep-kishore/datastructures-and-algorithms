# Fibonacci through iteration
def fibo(number):
    fibn_1, fibn, fibnp1 = 0, 1, 1
    count = 3
    while count < number:
        fib2n = (2 * fibn_1 + fibn) * fibn
        fib2np2 = (2 * fibn + fibnp1) * fibnp1
        fib2np1 = fib2np2 - fib2n
        fibn_1 = fib2n
        fibn = fib2np1
        fibnp1 = fib2np2
        count = count * 2 + 1
    print(count)
    count = (count-1) // 2
    if int(count - number) == 0:
        fib_final = fibn
    elif int(abs(count - number)) == 1:
        fib_final = fibnp1
    else:
        for dummy in range(int(count) + 2, int(number) + 1):
            fib_final = fibn + fibnp1
            fibn = fibnp1
            fibnp1 = fib_final
    # fib_list = [fibn, fibnp1, fib_final]
    # print(fib_list)
    return fib_final
