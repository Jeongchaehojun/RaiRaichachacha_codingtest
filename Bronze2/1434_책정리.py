#2025.07.29
#b2
N, M = map(int, input().split())

box_sizes = list(map(int, input().split()))
total_box_space = sum(box_sizes)

book_sizes = list(map(int, input().split()) )
total_book_size = sum(book_sizes)

# 남은 빈 공간 = 총 상자 공간 - 총 책 크기
remaining_space = total_box_space - total_book_size

print(remaining_space)
