#하늘에서 떨어지는 N개의 별
#2025.05.07
#시뮬레이션 기반 그리디 알고리즘
#
def min_cleanups(n, d, k, s):
    star = [0] * n  # 각 지점에 쌓인 별
    clean_count = 0

    for day in range(d):
        # 밤에 별 떨어짐
        for i in range(n):
            star[i] += s[i]

        # 폭발 조건 검사
        if any(star[i] > k for i in range(n)):
            clean_count += 1
            star = [0] * n  # 청소

    return clean_count

# 입력 처리
n, d, k = map(int, input().split())
s = list(map(int, input().split()))

# 결과 출력
print(min_cleanups(n, d, k, s))
