#!/usr/bin/env python3
import sys
if len(sys.argv) < 3:
    print("none") 
else:
    for index in range(len(sys.argv)-1, 0, -1):
        print(sys.argv[index],end=" ")
