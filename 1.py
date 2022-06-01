#!/usr/bin/python3
import sys
infile = sys.argv[1] if len(sys.argv) > 1 else '1.in'
X = [int(x) for x in open(infile)]
i = 0
S = {}
s = 0
while True:
    s += X[i]
    if s not in S:
        S[s] = 1
    else:
        print(s)
        break

    i += 1
    if i >= len(X):
        i = 0
