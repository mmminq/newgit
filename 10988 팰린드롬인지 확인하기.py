#10988

w = list(input())
temp = w.copy()
w.reverse()
if temp == w:
    print('1')
else:
    print('0')