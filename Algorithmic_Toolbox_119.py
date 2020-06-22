# Uses python3
# Week 4, 1 Binary Search

import sys

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    i = 0
    R = right - 1
    if x == a[0]:
        return 0
    if x == a[-1]:
        return R
    m = int ((right-left)/2)
    while (x > a[left]) and (x < a[R]):
        if a[m] == x:
            return m
            break
        elif a[m] > x:
            right = m
            R = right + 1
            m = int ((right-left)/2)
            M = m
        else:
            left = m
            M = int ((right-left)/2)
            m = M + m
        if M == 0:
            break
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    #for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
    #print('h')
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')

