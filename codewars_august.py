######################################################################


### 1
### Playing with digits

def dig_pow(n, p):
    """Given an integer, calculate if k exists such that
    the sum of the digits of n taken to the successive powers of
    p is equal to k * n, else return -1.
    (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
    
    Return:
        k: sum / n
        -1: if k is not an integer"""

    sum = 0

    for digit in str(n):
        sum += int(digit) ** p
        p += 1

    k = sum / n

    if k.is_integer() == True:
        return int(k)
    else:
        return -1


######################################################################






