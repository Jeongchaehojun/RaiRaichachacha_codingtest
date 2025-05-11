#2025.05.11
#bronze 5
n = int(input())
for i in range(1, n+1): #포멧에 번호 붙여야해서 1부터임
    A, B = map(int, input().split())
    print(f"Case #{i}: {A+B}")
    #f{}는 포멧팅 문법인데 
    #"Case #%d: %d %(i,A+B)" <- 옛날방식
    #"Case #{}: {}".format(i,A+B) <- str.format()
    #f"Case #{i}: {A+B}" <- 최신방식