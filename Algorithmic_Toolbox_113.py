# Uses python3
# Week 3, 2 Maximum Value of the Loot
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    PerUnit = []
    for x, y in zip(values, weights):
        if x!=0 and y!=0:
            PerUnit.append(x/y)
        else:
            PerUnit.append(0)
    import numpy
    a = numpy.argsort(PerUnit)
    b = a[::-1]
    for i in b:
        if values[i] == 0 or weights[i] == 0:
            continue
        m =  capacity - weights[i]
        if m <= 0:
            value = value + capacity*PerUnit[i]
            capacity = 0
        else:
            value = value + values[i]
        capacity =  capacity - weights[i]
        if capacity <= 0:
                break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
