import math


def get_gcd(a, b):
    if b > a:
        a, b = b, a
    while True:
        if b == 0:
            break
        q, r = divmod(a, b)
        a, b = b, r
    return a


def solution(w,h):
    # 8 12
    answer = 1
    gcd = get_gcd(w,h) # 4
    wlen = w // gcd
    hlen = h // gcd
    if wlen < hlen:
        wlen, hlen = hlen, wlen
    blanksum = 0
    for i in range(1, hlen):
        blanksum += 2 * (wlen - math.ceil(wlen/hlen * i ))

    ect = (wlen * hlen - blanksum) * gcd
    return w*h - ect


aa = solution(3,4)
print(aa)