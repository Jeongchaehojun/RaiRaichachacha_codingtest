#2025.08.17 오늘 2개 푼다
#g4
#이진 탐색 트리임

# 골드 승격전
import sys
sys.setrecursionlimit(10**6)
preOrder = []
while True:
    line = sys.stdin.readline().strip()
    if not line: #빈 줄이면 종료
        break
    preOrder.append(int(line)) #리스트에 정수값으로 넣기

#재귀임
def postOrder(start, end):
    if start >= end: #값이 없으면 종료
        return
    root = preOrder[start] #첫 번째 값은 루트.
    mid = start + 1 #오른쪽 서브트리 시작 위치 인덱스 초기화

    #루트보다 큰 값이 나타나는 지점까지 mid 이동시키기
    while mid < end and preOrder[mid] < root:
        mid += 1

    #여기서 재귀
    postOrder(start + 1, mid)
    postOrder(mid, end)
    print(root)

#전체 구간 후위 순회
postOrder(0, len(preOrder))