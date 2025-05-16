#2025.05.16
#b5
t1, e1, f1 = map(int, input().split())
t2, e2, f2 = map(int, input().split())
smax = t1*3 + e1 * 20 + f1 * 140
mel = t2*3 + e2 * 20 + f2 * 140
if smax > mel:
    print("Max")
elif smax < mel:
    print("Mel")
elif smax == mel:
    print("Draw")