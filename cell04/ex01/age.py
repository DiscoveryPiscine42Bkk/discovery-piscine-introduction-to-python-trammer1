#!/usr/bin/env python3
inp = int(input("Please tell me your age: "))
print(f"Your are currently {inp} years old.")
for i in range(1,4):

    print(f"In {i*10} year(s) you will be {inp + (i*10)} years old.")
    i += 1
