#백준 2475번 검증수
#2025.05.08
#브론즈5
#다섯 개 수가 오면 각 수를 제곱해서 더하고 10으로 나눈 수의 나머지를 출력
hap = sum(int(x)**2 for x in input().split())
print(hap%10)

"""
리스트로 표현:
hap = list(map(int(),input().split()))
total = sum((x)**2 for x in hap)
print(total%10)
"""