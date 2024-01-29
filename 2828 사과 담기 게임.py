#2828

n, m = map(int, input().split())
j = int(input())
l = 0
left=1
right=m
for _ in range(j):
    a = int(input())
    
    if a<left:
        temp = left-a
        left -= temp
        right -= temp
        l += temp
    elif a>right:
        temp = a-right
        left += temp
        right += temp
        l += temp
    else:
        pass

print(l)