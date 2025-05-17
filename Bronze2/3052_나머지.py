#2025.05.17
#b2
temp = []
for _ in range(10):
    n = int(input())
    temp.append(n%42)
    
print(len(set(temp)))
#set()은 중복을 제거해줘요!