def PerfectSQ(x):
    #while - SQR num,divide num by SQR'd num.if remainder,-1 else ret num given
    while (x % x**0.5) != 0:
        x-=1
    return x

