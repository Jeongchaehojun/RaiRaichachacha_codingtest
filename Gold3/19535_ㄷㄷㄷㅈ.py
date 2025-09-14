#2025.09.14
#g3
#tree
#어제 까먹은거 개오바임;;

import sys
from math import comb
input = sys.stdin.readline

n = int(input())
node_list = [0] * (n+1)

edge_list = []

for _ in range(n-1):
    u, v = map(int, input().split())
    node_list[u] += 1
    node_list[v] += 1
    edge_list.append((u,v))

dd_tree = 0 #ㄷ 트리 개수
gg_tree = 0 #ㅈ 트리 개수

#ㄷ 트리 개수 계산
for u, v in edge_list:
    dd_tree += (node_list[u] - 1) * (node_list[v] - 1)

#ㅈ 트리 개수 계산
for i in range(1, n+1):
    if node_list[i] >= 3:
        gg_tree += comb(node_list[i], 3)

if dd_tree > 3 * gg_tree:
    print("D")
elif dd_tree < 3 * gg_tree:
    print("G")
else:
    print("DUDUDUNGA")