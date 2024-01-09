#2798

n, m = map(int, input().split())
num = list(map(int, input().split()))

total = 0

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            t_total = num[i] + num[j] + num[k]
            if t_total <= m and t_total > total:
                total = t_total
            
print(total)