# Uses python3
# Week 2, 6 Last Digit of the Sum of Fibonacci Numbers

import sys

def MatrixPower(A, x):
    result = np.identity(2)
    while x > 0:
        if x % 2 == 1:
            result = np.matmul(result%m,A%m)
        A = np.matmul(A%m, A%m)
        x = x // 2
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
m =10
import numpy as np
n = n+2
A = [[1,1],[1,0]]
A = np.array(A)
B = MatrixPower(A, n)%m
if int (B[0][1]-1) < 0:
    print (int (B[0][1]-1)+10)
else:
    print (int (B[0][1]-1))
