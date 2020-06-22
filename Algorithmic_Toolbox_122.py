# Uses python3
# Week 5, 1 Money Change Again
import sys

def get_change(m):
    #write your code here
    coins = [1, 3, 4]
    minCoin=[0]*1000
    minCoin[0] = 0
    if m == 0:
        return 0
    for i in range(1, m+1):
        minCoin[i] = float('Inf')
        for j in coins:
            if j <= m:
                if minCoin[i-j] + 1 < minCoin[i]:
                    minCoin[i] = minCoin[i-j] + 1
    return minCoin[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
