#2025.06.29
#b1
n = int(input())
filenames = [input().strip() for _ in range(n)]

pattern = list(filenames[0])

for fname in filenames[1:]:
    for i in range(len(fname)):
        if pattern[i] != fname[i]:
            pattern[i] = '?'

print(''.join(pattern))
