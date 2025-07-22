#2025.07.22
#b2
import sys

A, B = sys.stdin.readline().split()

total = 0
for a in A:
    for b in B:
        total += int(a) * int(b)

print(total)
