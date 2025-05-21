#2025.05.21
#b2
L = int(input())
word = input().strip()

r = 31
M = 1234567891

hash = 0

#ord()는 문자하나를 유니코드 정수 값으로 돌려줌. ord('a')는 97
#ord(i) - ord('a') + 1 이거 쓰면 abcdef.. 이게 12345...
for i in range(L):
    char = ord(word[i]) - ord('a') + 1
    hash += char * (r**i)

print(hash%M)