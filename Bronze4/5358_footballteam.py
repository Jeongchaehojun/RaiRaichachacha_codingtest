#2025.05.21
#b4
import sys
for line in sys.stdin:
    name = line.strip()
    new_name = ''
    for ch in name:
        if ch not in ['i', 'e', 'I', 'E']:
            new_name += ch
        elif ch == 'i':
            ch = 'e'
            new_name += ch
        elif ch == 'e':
            ch = 'i'
            new_name += ch
        elif ch == 'I':
            ch = 'E'
            new_name += ch
        elif ch == 'E':
            ch = 'I'
            new_name += ch
    print(new_name)