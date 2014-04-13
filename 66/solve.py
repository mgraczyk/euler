#!/usr/bin/python3

import sys

import gmpy2
from gmpy2 import mpz
from gmpy2 import isqrt
from gmpy2 import sub
from gmpy2 import mul
from gmpy2 import div
from gmpy2 import t_divmod
from gmpy2 import is_square

from itertools import count

def minx(D):
    x = isqrt(D)
    zero = mpz(0)
    while 1:
        ysq, rem = t_divmod(x*x - 1,D)
        if rem == zero and is_square(ysq):
            print(x, isqrt(ysq))
            return x
        x += 1

def minxfromy(D):
    y = 1
    ysq = y*y

    while 1:
        xsq = 1 + D*ysq
        if is_square(xsq):
            x = isqrt(xsq)
            return x
        ysq += 2*y + 1
        y += 1

def argminxD(D):
    return max((mpz(d) for d in range(1, D + 1) if not is_square(d)), key=minxfromy)

if __name__ == "__main__":
    print(argminxD(mpz(sys.argv[1])))


