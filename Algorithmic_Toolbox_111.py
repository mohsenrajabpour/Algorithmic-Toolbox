# Uses python3
# Week 2, 8 Last Digit of the Sum of Squares of Fibonacci Numbers
from sys import stdin

def calc_fib2(n):
    A = 1
    B = 1
    C = 0    
    for i in bin(n)[3:]:  
        A, B, C = (A**2 + B**2)%10, (A*B + B*C)%10, (B**2 + C**2)%10
        if i == '1':
            A, B, C = (A + B)%10, A%10, B%10
    return B

if __name__ == '__main__':
    n = int(stdin.read())
    if n == 0:
       c = n
    else:
        a = calc_fib2(n)
        b = calc_fib2(n+1)
        c = (a*b)%10
        if int (c) < 0:
            c = int(c)+10
    print (c)
