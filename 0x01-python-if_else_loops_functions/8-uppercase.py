#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) > 96 and ord(a) < 123:
            a = chr(ord(a) - 32)
            print(a, end='')
        else:
            print(a, end='')
    print()
