#10539

n = int(input())
b = list(map(int, input().split()))
for i in range(0, n):
    b[i] = b[i]*(i+1)
a = []
for i in range(n-1, 0, -1):
    a.insert(0, b[i]-b[i-1])
a.insert(0, b[0])

for i in a:
    print(i, end=' ')
print('\b')