#2025.06.24
#b3
while True:
    n = input()
    if n == '0':
        break
    width = 0
    for i in n:
        if i == '0':
            width += 4
        elif i == '1':
            width += 2
        else:
            width += 3
    width += len(n) - 1  # 숫자 사이 여백
    width += 2  # 양쪽 끝 여백
    print(width)
