#!/usr/bin/python3
from add_0.py import add(a, b):
a = 1
b = 2
add_0 ={}
exec(open("add_0.py") .read(), add_0)
print("{:d} + {:d} = {:d}" .format(a, b, add_0['add'](a,b)))
