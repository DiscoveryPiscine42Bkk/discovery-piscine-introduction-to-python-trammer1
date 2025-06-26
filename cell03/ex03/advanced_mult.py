#!/usr/bin/env python3
num = 0
while num <= 10:
    print(f"Table de {num}:", end=" ")
    start = 0
    while start <= 10:
        print(f"{num * start}", end="\n" if start == 10 else " ")
        start += 1
    num += 1
