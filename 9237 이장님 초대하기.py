# 9237
n = int(input())

days = list(map(int, input().split()))
days.sort(reverse=True)

for i in range(len(days)):
    days[i]+=i+1
    
print(max(days)+1)