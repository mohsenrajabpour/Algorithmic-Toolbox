#Uses python3
# Week 3, 7 Maximum Salary

import sys

def largest_number(a):
    A = []
    B = []    

    A = list(map(int, a))
    while len(A)>0:
        MX = A[0]
        for i in range(1, len(A)):
            FC = str(MX) + str(A[i])
            SC = str(A[i]) + str(MX)
            if int(SC) > int(FC):
                MX = A[i]
        B.extend([MX])
        A.remove(MX)
    B = list(map(str, B))
    res = ""
    for x in B:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
