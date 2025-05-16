#2025.05.16
#b3
#소거법으로 가보자.
studendts = set(range(1, 31))

for _ in range(28):
    sub = int(input())
    studendts.remove(sub)
two = sorted(studendts)
print(two[0])
print(two[1])