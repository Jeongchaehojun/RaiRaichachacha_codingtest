#2025.09.09
#s5
import sys
input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))

M = int(input())
test = list(map(int, input().split()))

print(' '.join('1' if num in cards else '0' for num in test))