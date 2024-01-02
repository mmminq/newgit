#1120

def comp(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt

a, b = input().split()
min_comp = len(b)

for i in range(len(b)-len(a)+1):
    if min_comp > comp(a, b[i:i+len(a)]):
        min_comp = comp(a, b[i:i+len(a)])
        
print(min_comp)