#2979

a, b, c = map(int, input().split())
truck = []
for _ in range(3):
    n = list(input().split())
    truck.append(n)

dic = dict()

for i in truck:
    for j in range(int(i[0])+1, int(i[1])+1):
        if str(j) not in dic.keys():
            dic[str(j)] = 1
        elif str(j) in dic.keys():
            dic[str(j)] += 1
                
total = 0
for i in dic.values():
    if i == 0:
        pass
    elif i == 1:
        total += a
    elif i == 2:
        total += b*2
    elif i == 3:
        total += c*3
        
print(total)