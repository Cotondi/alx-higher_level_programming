#!/usr/bin/python3
for o in range(9):
    for t in range(o + 1, 10):
        print("{:d}{:d}".format(o, t), end=(", " if not (o == 8 and t == 9)
        else "\n"))
