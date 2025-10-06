#2025.10.06
#b1
import sys

input = sys.stdin.read

data = input().splitlines()
n = int(data[0])

for i in range(1, n + 1):
    scores = list(map(int, data[i].split()))
    count = scores[0]
    grades = scores[1:]
    average = sum(grades) / count
    above_average = [score for score in grades if score > average]
    percentage = (len(above_average) / count) * 100
    print(f"{percentage:.3f}%")