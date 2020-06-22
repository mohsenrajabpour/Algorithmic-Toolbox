# Uses python3
# Week 3, 6 Maximum Number of Prizes
import sys

def optimal_summands(n):
    summands = []
    
    #write your code here
    summands.append(1)
    n = n-1
    i = 1
    while n-summands[i-1]>0:
        summands.append(i+1)
        n = n-(i+1)
        i += 1
    summands[-1] = summands[-1] + n
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
