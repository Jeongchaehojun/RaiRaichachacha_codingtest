#2025.10.25
#b2
nums = [int(input().strip()) for _ in range(5)]

average = sum(nums) // 5

# 중앙값
nums.sort()
median = nums[2]

print(average)
print(median)
