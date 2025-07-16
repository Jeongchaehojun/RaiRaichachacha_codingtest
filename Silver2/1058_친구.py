#2025.07.16
#s2
'''N = int(input())
friends = [int() for _ in range(N)]''' #이거 런타임 에러남..

import sys
N = int(sys.stdin.readline())
friends = [sys.stdin.readline().strip() for _ in range(N)]

maxfriends = 0

for i in range(N):
    two_friends = set()

    for j in range(N):
        if i == j:
            continue

        if friends[i][j] == 'Y':
            two_friends.add(j)

            for k in range(N):
                if j == k or i == k:
                    continue

                if friends[j][k] == 'Y':
                    two_friends.add(k)
    friends_count = len(two_friends)
    if friends_count > maxfriends:
        maxfriends = friends_count
print(maxfriends)