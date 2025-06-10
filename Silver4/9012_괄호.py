#2025.06.10
#s4
#자료구조 주제의 코드임 "STACK"
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    s = sys.stdin.readline().strip()
    cnt =0
    ok = True
    for ch in s:
        if ch == '(':
            cnt += 1
        else: 
            cnt -= 1

        if cnt <0:
            ok = False
            break
    if cnt != 0:
        ok = False
    print("YES" if ok else "NO")

#만약 여러 종류의 괄호 [{()}] 가 필요하면 cnt가 아니라 스택이 필요
"""
stack = []
for ch in s:
    if ch == '(':
        stack.append(ch)
    elif ch == ')':
        if not stack:
            return "NO"
        stack.pop()

"""
