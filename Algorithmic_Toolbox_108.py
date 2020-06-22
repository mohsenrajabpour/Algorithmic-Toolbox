# Uses python3
# Week 2, 5 Fibonacci Number Again
 
import sys

def MatrixPower(A, x):
    result = np.identity(2)
    while x > 0:
        if x % 2 == 1:
            result = np.matmul(result%m,A%m)
        A = np.matmul(A%m , A%m)
        x = x // 2
    return result

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    
import numpy as np
A = [[1,1],[1,0]]
A = np.array(A)
B = MatrixPower(A , n)%m
print (int (B[0][1]))

'''def Huge_Fib(n,m):

    # Initialize a matrix [[1,1],[1,0]]    
    v1, v2, v3 = 1, 1, 0  
    # Perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n)[3:]:
        calc = (v2*v2) % m
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
    print(v2);        

n,m = map(int, input().split());   
Huge_Fib(n,m);'''
