#!/usr/bin/python3
for i in range(100):
        if i > 98:
                print(f"{i:d}", end='\n')
        else:
                print(f"{i:0>2}", end=', ')
