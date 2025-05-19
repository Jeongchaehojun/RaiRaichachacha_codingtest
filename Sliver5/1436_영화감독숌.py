#2025.05.19
#s5
N = int(input())

count = 0
jongmal = 666

while True:
    if '666' in str(jongmal):
        count+=1
        if count == N:
            print(jongmal)
            break
    jongmal += 1