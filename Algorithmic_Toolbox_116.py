# Uses python3
#Week 3, 5 Collecting Signatures
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort(key=lambda x: x[1])
    points.append(segments[0][1])
    for i in range (len (segments)):
        if segments[i][0] > points[-1]:
            points.append(segments[i][1])

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
