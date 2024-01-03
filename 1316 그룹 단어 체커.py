#1316

n = int(input())
cnt = 0
for i in range(n):
    dic = []
    breaker = 0
    a = input()
    for i in a:
        if i not in dic:
            dic.append(i)
        elif i in dic and i != dic[-1]:
            breaker = 1
            break
        else:
            continue
    if breaker == 1:
        continue
    cnt += 1

print(cnt)