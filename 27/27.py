from math import *

data = [tuple(map(float, f.split())) for f in open('27_A_18884.txt')]
clusters = []
while data:
    clusters.append([data.pop()])
    for p1 in clusters[-1]:
        for p2 in data[:]:
            if dist(p1, p2) <20:
                clusters[-1].append(p2)
                data.remove(p2)
