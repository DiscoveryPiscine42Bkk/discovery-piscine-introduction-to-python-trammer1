#!/usr/bin/env python3
num = input("Give me a number: ")
try:
    number = float(num)
    if number == int(number):
        print(int(number))
    else:
        print(int(number) + 1)
except ValueError:
    print("Invalid Input!")