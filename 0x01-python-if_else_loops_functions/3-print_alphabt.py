#!/usr/bin/python3
for chars in range(ord('a'), (ord('z')) + 1):
    if chr(chars) not in ['q', 'e']:
        print("{:}".format(chr(chars)), end='')
