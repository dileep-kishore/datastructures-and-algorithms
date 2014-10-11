'''Fast expo'''
import time
def fast_expo(x,n):
    bin_n = bin(n)
    bin_n = bin_n[2:]
    bin_length = len(bin_n)
    current_exponent = x
    answer = 1
    for ind in range(bin_length-1,-1,-1):
        if bin_n[ind] == '1':
            answer *= current_exponent
        current_exponent *= current_exponent
    return answer
t1 = time.perf_counter()
print(fast_expo(10**500,500))
t2 = time.perf_counter()
print((t2-t1)*1000)