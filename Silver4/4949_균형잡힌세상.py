#2025.06.11
#s4
#괄호 쓰는 스택임
import sys

def is_balanced(line):
    stack = []
    for ch in line:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
    return not stack

if __name__ == "__main__":
    while True:
        line = sys.stdin.readline().rstrip()
        if line == '.':
            break
        if is_balanced(line):
            print("yes")
        else:
            print("no")