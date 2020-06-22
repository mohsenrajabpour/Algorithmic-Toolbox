# Uses python3
# Week 2, 7 Last Digit of the Sum of Fibonacci Numbers Again

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
    input = sys.stdin.read();
    from_, to = map(int, input.split())
m =10
import numpy as np
to = to+2
from_ = from_ + 1
A = [[1,1],[1,0]]
A = np.array(A)
B = MatrixPower(A, to)%m
if int (B[0][1]-1) < 0:
    BB = int(B[0][1]-1)+10
else:
    BB = int(B[0][1]-1)

C = MatrixPower(A, from_)%m
if int (C[0][1]-1) < 0:
    CC = int(B[0][1]-1)+10
else:
    CC = int(C[0][1]-1)

print((BB - CC)%10)
