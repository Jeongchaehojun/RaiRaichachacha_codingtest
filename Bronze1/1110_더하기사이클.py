#2025.07.18
#b1
#진짜 장염걸렸는데 죽을 것 같음
n = int(input())
origin = n
cnt = 0

while True:
    a = n//10
    b = n%10
    s = (a+b) % 10

    n = b * 10 + s
    cnt +=1

    if n == origin:
        print(cnt)
        break