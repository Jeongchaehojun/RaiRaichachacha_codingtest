#2025.05.12
#b5
A, B = map(int, input().split())
#중요한건 톰이 1kg인데 그건 B/B임
#따라서 분자: B-A, 분모: B
print(B-A, end = ' ')
print(B)