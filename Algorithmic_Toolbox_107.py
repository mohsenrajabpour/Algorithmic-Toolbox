# Uses python3
# Week 2, 4 Least Common Multiple

import sys

def lcm_naive(a, b):
    
    n = a
    m = b
    
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
    l = (n*m)//c
    return l

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

