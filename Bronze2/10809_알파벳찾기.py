#2025.05.18
#b2
#let's start morning coding
S = input().strip()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
sol = []

for ch in alphabet:
    sol.append(str(S.find(ch)))
print(' '.join(sol))

#sol.append(str(S.find(ch))) 받은 문자열을 한 글자씩 가면서 없으면 -1을 반환하고 있으면
#처음 나오는 인덱스를 반환한다. 근데 그걸 문자열로 리스트에 append한다
#join은 리스트 안의 요소를 하나의 문자열로 이어붙인다 ' ' 를 통해 공백을 추가해줌
    