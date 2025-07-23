#2025.07.23
#s4
import sys
input = sys.stdin.readline

n = int(input().strip())
borr = {} #borrow

for _ in range(n):
    book = input().rstrip() # 책 제목이 1열로 나열됨
    borr[book] = borr.get(book, 0) + 1

items = [(cnt, title) for title, cnt in borr.items()]

items.sort(key=lambda x: (-x[0], x[1]))

print(items[0][1])