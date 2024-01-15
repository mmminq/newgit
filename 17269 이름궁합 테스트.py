#17269

n, m = map(int, input().split())
a, b = input().split()
arr = []
cnt = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

for i in range(min(n, m)):
    arr.append(a[i])
    arr.append(b[i])
    
if n<m:
    for i in b[m-n:]:
        arr.append(i)
elif n>m:
    for i in a[n-m:]:
        arr.append(i)
        
for i in range(len(arr)):
    temp = ord(arr[i])
    arr[i] = cnt[temp-65]
    
'''while len(arr) > 2:
    temp_arr = []
    for i in range(len(arr)-1):
        temp_arr.append((arr[i]+arr[i+1])%10)
    arr = temp_arr'''