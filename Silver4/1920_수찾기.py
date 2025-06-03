#2025.06.03
#s4
#binary search 알고리즘
""" import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort() #정렬 해준 다음에 탐색

M = int(input())
targets = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for t in targets:
    print(binary_search(A, t)) """
#이 위는 시간 복잡도 O(N logN)

import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split())) #리스트를 set으로
#set을 쓰면 {1,2,3,4,5} 이런 식으로 진행됨
M = int(input())
targets = list(map(int, input().split()))

for t in targets:
    print(1 if t in A else 0) #포함되면 1, 없으면 0입니다.

#이 위는 시간 복잡도 O(N+M)