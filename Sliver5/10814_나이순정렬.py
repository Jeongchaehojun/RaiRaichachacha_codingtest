#2025.05.28
#s5
import sys
input = sys.stdin.readline

N= int(input())
members = []

for _ in range(N):
    age, name = input().split()
    members.append((int(age),name)) #튜플()로 묶어줘야합니다.

members.sort(key=lambda x: x[0])
for age, name in members:
    print(age, name)