# Fast exponentiation
import time
def fast_expo(number, power):
    ''' number^power using fast exponentiation'''
    time1 = time.perf_counter()
    pow_bin = bin(power)
    pow_bin = pow_bin[2:]
    power_bin = list(reversed(pow_bin))
    pos = 0
    answer = 1
    square = number ** 2
    print(power_bin)
    for dummy in power_bin:
        if dummy == '1':
            dummy2 = 2 ** pos
            while dummy2 > 1:
                answer *= square
                dummy2 -= 2
        pos += 1
    if power % 2 == 1:
        answer *= number
    time2 = time.perf_counter()
    print('time taken:', (time2-time1)*1000, 'ms')
    return answer
