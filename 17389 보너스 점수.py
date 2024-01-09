#17389

n = int(input())

arr = list(input())
total = 0
bonus = 0

for i in range(n):
    if arr[i] == 'O':
        bonus += 1
        total += bonus
        total += i
    else:
        bonus = 0

print(total)