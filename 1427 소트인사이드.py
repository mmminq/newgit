#1427

num = list(map(str, input()))

num.sort(reverse=True)

for i in num:
    print(i,end='')