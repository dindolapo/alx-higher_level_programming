#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = str(number)
lastDigit = int(string[-1])

if number < 0:
    if lastDigit == 0:
        print(f"Last digit of {number:d} is {lastDigit:d} and is 0")
    else:
        print(f"Last digit of {number:d} is {lastDigit * (-1):d} and is less t\
han 6 and not 0")
elif lastDigit > 5:
    print(f"Last digit of {number:d} is {lastDigit:d} and is greater than 5")
elif lastDigit < 6 and lastDigit != 0:
    print(f"Last digit of {number:d} is {lastDigit:d} and is less then 6 and\
 not 0")
else:
    print(f"Last digit of {number:d} is {lastDigit:d} and is 0")
