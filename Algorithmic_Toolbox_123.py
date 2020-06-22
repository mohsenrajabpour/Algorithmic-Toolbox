# Uses python3
# Week 5, 2 Primitive Calculator
import sys

def optimal_sequence(n):
    
    S = [0]*(n+1)
    MinOperations = [0]*(n+1)

    for i in range(1, n+1):
        s = i - 1
        MO = MinOperations[i-1] + 1

        if i % 3 == 0:
            NuOp = MinOperations[i//3] + 1
            if NuOp < MO:
                s = i//3
                MO = NuOp

        if i % 2 == 0:
            NuOp = MinOperations[i//2] + 1
            if NuOp < MO:
                s = i//2
                MO = NuOp

        S[i] = s
        MinOperations[i] = MO
    #############
    sequence = []
    k = n
    while k > 0:
        sequence.append(k)
        k = S[k]
    sequence.reverse()

    return  sequence

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

