#2025.05.27
#s5
#규칙: 길이가 짧은 순 -> 길이가 같으면 사전순 -> 중복 단어는 하나 남기고 제거
N = int(input())
words = set() #중복 제거

for _ in range(N):
    word = input().strip()
    words.add(word)

sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)
