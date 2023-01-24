#!/usr/bin/python3
def print_last_digit(number):
    string = str(number)
    lastDigit = int(string[-1])
    print(lastDigit, end='')
    return lastDigit
