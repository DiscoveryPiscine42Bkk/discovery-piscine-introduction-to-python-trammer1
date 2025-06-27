#!/usr/bin/env python3
original =[2, 8, 9, 48, 8, 22, -12, 2]
newarray = []
for element in original:
    if element >= 5:
        newarray.append(element+2)
print("Original array:", original)
print("New array:", newarray)