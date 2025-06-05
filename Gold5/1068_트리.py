#2025.06.05
#G5
#트리 만드는 문제인데 연습하는 용으로 골드까지 연습
#dfs
n = int(input()) #트리의 노드 개수
p = list(map(int, input().split())) #각 노드의 부모를 입력받아 리스트 p에 저장
d = int(input()) #삭제할 노드 번호
t = [[] for _ in range(n)] #트리 구조 리스트 초기화
for i in range(n):
    if p[i] != -1:
        t[p[i]].append(i) #부모 p[i] 의 자식으로 i 추가
r = p.index(-1) #루트 노드는 부모가 -1인 노드

def dfs(x):
    if x == d:
        return 0 #삭제할 노드에 도착하면 서브트리 무시
    if not[c for c in t[x] if c != d]: 
        return 1
    return sum(dfs(c) for c in t[x] if c != d)
# 만약 삭제할 노드가 루트라면 트리 전체가 사라지므로 0 출력
# 그렇지 않으면 루트부터 DFS 탐색을 시작해 리프 노드 수 출력
print(0 if d == r else dfs(r))