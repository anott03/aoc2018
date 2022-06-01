#!/usr/bin/python3
import sys
infile = sys.argv[1] if len(sys.argv) > 1 else '2.in'
X = [x.strip() for x in open(infile)]
_2 = 0
_3 = 0
for x in X:
    for c in x:
        if x.count(c) == 2:
            _2 += 1
            break
    for c in x:
        if x.count(c) == 3:
            _3 += 1
            break
print(_2 * _3)

done = False
for x in X:
    for y in X:
        err_count = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                err_count += 1
            if err_count > 1:
                continue
        if err_count == 1:
            print(x)
            print(y)
            done = True
    if done:
        break
