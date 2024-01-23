#!/usr/bin/python3
a = 89
b = 10
a, b = (lambda x, y: (y, x))(a, b)  # a, b = b, a
print("a={:d} - b={:d}".format(a, b))
