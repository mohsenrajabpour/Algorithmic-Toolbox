# python3
# Week 3, 3 Car Fueling
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops = [0] + stops + [distance]
    a = []
    i = 1
    FD = distance
    while distance > tank:
        if stops[i]-stops[i-1] > m:
            return -1
        if stops[i]-stops[0] > tank:
            a.append(stops[i-1])
            distance = FD - stops[i-1]
            del stops[0:i-1]
            i = 0
        i += 1
    return len(a)

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
