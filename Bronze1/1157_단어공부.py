


#2025.07.21
#b1
word = input().strip().upper()
cnt = [0]*26

for ch in word:
    cnt[ord(ch) - ord('A')] += 1

max_count = max(cnt)
if cnt.count(max_count) > 1:
    print('?')
else:
    print(chr(cnt.index(max_count) + ord('A')))