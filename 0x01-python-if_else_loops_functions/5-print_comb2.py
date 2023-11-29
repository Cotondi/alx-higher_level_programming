#!/usr/bin/python3
for chars in range(100):
    print("{:02d}" .format(chars), end=(", " if chars < 99 else "\n"))
