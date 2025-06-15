#2025.06.15
#s4
#N 개 숫자카드 내역 중에 M개의 숫자카드 내역이 몇개씩 있는지 기록하기.

#collections.counter(해시맵)
import sys
from collections import Counter

input = sys.stdin.readline

def main():
    N = int(input())
    cards = list(map(int, input().split()))
    M = int(input())
    queries = list(map(int, input().split()))

    count = Counter(cards)
    print(' '.join(str(count[q]) if q in count else '0'for q in queries))
if __name__ == "__main__":
    main()