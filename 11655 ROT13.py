#11655

s = list(input())
ss = []
for i in s:
    ss.append(ord(i))
s = []
for i in ss:
    if i>=65 and i<=90:
        if i>=78:
            s.append(i-13)
            continue
        s.append(i+13)
        continue
    elif i>=97 and i<=122:
        if i>=110:
            s.append(i-13)
            continue
        s.append(i+13)
        continue
    else:
        s.append(i)
        
for i in s:
    print(chr(i), end='')