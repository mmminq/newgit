#5555

s = input()
n = int(input())
cnt = 0

for i in range(n):
    ss = input()
    sss = ss*2
    if s in sss: cnt += 1
    
print(cnt)