# Uses python3
# Week 2, 3 Greatest Common Divisor

import sys

def gcd_naive(a, b):
    i = 0
    while i == 0:
        a,b = max(a,b),min(a,b)
        c = a % b
        a,b = b,c
        if c == 0: 
            i = 1
            c = a
        elif ((c%b) < 0):
            i = 1
            c = b
    return c

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
