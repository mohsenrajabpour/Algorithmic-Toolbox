# Uses python3
# Week 4, 2 Majority Element
import sys
import numpy as np

'''def get_majority_element(a, left, right):
    import numpy
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here'''
# Third method 
def get_majority_element(a):
    if(len(a) == 1):
        return a[0]
    
    m = len(a)//2
    left = a[:m] 
    right = a[m:]
    
    Left  = get_majority_element(left)
    Right = get_majority_element(right) 
    if Left == Right: 
        return Left
    if a.count(Left)> m: 
        return Left
    if a.count(Right)> m: 
        return Right
    return -1

    # First method, but it didn't pass the test
    '''a.sort()
    res = -1
    for i in range(0, int(n/2)):
        if a[i] == a[i+int(n/2)]:
            res = 1

    return res'''
    # Second method, but it didn't pass the test
    '''for i in range(0, len(a)):
        current = a[i]
        Array = numpy.array(a)
        inds = numpy.where(Array == current)
        res = Array[inds]
        if len (res) > round (len(a)/2):
            final = 1
            break
        else:
            final = -1
    return final '''

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    '''if get_majority_element(a, 0, n) != -1:'''
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)

