#Uses python3
#Week 3, 4 Maximum Advertisement Revenue

import sys

def max_dot_product(a, b):
    #write your code here
    a = sorted(a)
    b = sorted(b)
    c = [x*y for x,y in zip(a,b)]
    res = sum(c)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
