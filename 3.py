#!/usr/bin/python3
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "3.in"

X = [line for line in open(infile)]
M = [[0 for _ in range(1000)] for __ in range(1000)]

for l in X:
    x = l.strip().split(" ")[2:]
    s = [int(z) for z in x[0][:-1].split(',')]
    d = [int(z) for z in x[1].split('x')]

    for i in range(s[0], s[0] + d[0]):
        for j in range(s[1], s[1] + d[1]):
            M[i][j] += 1

c = 0
for r in M:
    for e in r:
        if e > 1:
            c += 1

print(c)
