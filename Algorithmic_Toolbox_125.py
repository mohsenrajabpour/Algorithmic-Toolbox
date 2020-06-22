#Uses python3
# Week 5, 4 Longest Common Subsequence of Two Sequences
import sys

def lcs2(a, b):
    m = len(a) 
    n = len(b) 
    import numpy as np
    M = np.zeros((m+1, n+1))
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                M[i][j] = 0
            elif a[i-1] == b[j-1]: 
                M[i][j] = M[i-1][j-1]+1
            else: 
                M[i][j] = max(M[i-1][j] , M[i][j-1]) 
  
    return int(M[m][n])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
