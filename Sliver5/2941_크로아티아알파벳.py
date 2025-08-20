#2025.08.21
#s5
#살짝 지쳐서 쉬운 구현 문제 탐색했어요

word = input().strip()

alphaC = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in alphaC:
    word = word.replace(c, "@")
print(len(word))

#replace로 치환하는 아이디어가 레전드 
