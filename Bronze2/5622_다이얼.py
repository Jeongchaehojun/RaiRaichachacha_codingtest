#2025.08.22
#b2
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input().strip()

time = 0
for ch in word:
    for idx, group in enumerate(dial):
        if ch in group:
            time += idx + 3
            break

print(time)