#!/usr/bin/python3
for i in range(100):
    if i > 98:
        print("{:d}".format(i), end='\n')
    else:
        print("{:0>2}".format(i), end=', ')
