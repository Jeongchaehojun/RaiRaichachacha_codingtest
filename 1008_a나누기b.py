# 백준 1008번 
#A/B 구하기
"""
def solution(n1, n2):
    return n1 / n2
"""
# 위 방법은 프로그래머스에서 함수형으로 통할 수는 있어도 백준에서 입출력 형태에서 안통함
A, B = map(int, input().split())
print(A/B)