#2025.05.17
#b2
"""
T = int(input())
for i in range(T):
    chong = input().strip()
    score = 0
    cnt = 0
    for ch in chong:
        if ch == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
"""
T = int(input)
for _ in range(T):
    chong = input().split('X')
    score = 0
    for group in chong:
        length = len(group)
        score += length * (length + 1) // 2
    print(score)

#근데 문자열로 받으면 시간복잡도 올라감.