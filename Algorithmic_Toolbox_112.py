# Uses python3
# Week 3, 1 Money Change
import sys

def get_change(m):
    #write your code here
    N = 0
    a = [10, 5, 1]
    for i in range(0,len(a)):
        n = int (m /a[i])
        N = N +n
        m = m%a[i]
    return N

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
