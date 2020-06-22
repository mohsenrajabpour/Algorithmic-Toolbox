# Uses python3
# Week 6, 1 Maximum Amount of Gold
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    import numpy as np
    n = len(w)
    value = np.zeros((W+1, n+1))
    
    for i in range(1, n+1):
        for j in range(1, W+1):
            value[j][i] = value[j][i-1]
            if w[i-1] <= j:
                val = value [j-w[i-1]][i-1] + w[i-1]
                if value[j][i] < val:
                    value[j][i] = val

    result = int(value[W][n])
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
