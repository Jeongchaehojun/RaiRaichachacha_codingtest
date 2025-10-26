#2025.10.26
#s2
#산술평균, 중앙값, 최빈값, 범위 하는건데 으렵다 으려워
from collections import Counter

n = int(input())
nums = [int(input()) for _ in range(n)]

avg = round(sum(nums) / n) #산술 평균

nums.sort()
mid = nums[n // 2] #중앙값

cnt = Counter(nums).most_common()

if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    mode = cnt[1][0] #최빈값
else:
    mode = cnt[0][0]    

ran = nums[-1] - nums[0] #범위

print(avg)
print(mid)
print(mode)
print(ran)  
