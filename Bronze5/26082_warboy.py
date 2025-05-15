#2025.05.15
#b5
A, B, C = map(int, input().split()) #경쟁사 가격, 경쟁사 성능, 워보이 가격
#warboy 가격대비 성능은 경쟁사의 3배
x = 0 #warboy 성능
x = (B // A)*3*C
print(x)