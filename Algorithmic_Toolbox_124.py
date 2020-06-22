# Uses python3
# Week 5, 3 Edit Distance
def edit_distance(s, t):
    #write your code here
    import numpy as np
    m = len(s)
    n = len(t)
    M = np.zeros((m+1, n+1))
    for i in range(0, m+1):
        for j in range(0, n+1):
            if i == 0:
                M[i][j] = j
            elif j == 0:
                M[i][j] = i
            elif s[i-1] == t[j-1]:
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = 1 + min(M[i][j-1], M[i-1][j], M[i-1][j-1])
                
    return int(M[m][n])#0

if __name__ == "__main__":
    print(edit_distance(input(), input()))
