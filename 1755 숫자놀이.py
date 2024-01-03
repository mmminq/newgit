#1755
def num_to_str(n):
    if n == 0: return 'zero'
    elif n == 1: return 'one'
    elif n == 2: return 'two'
    elif n == 3: return 'three'
    elif n == 4: return 'four'
    elif n == 5: return 'five'
    elif n == 6: return 'six'
    elif n == 7: return 'seven'
    elif n == 8: return 'eight'
    else: return 'nine'
    
def readnumber(n):
    if n<10: return num_to_str(n)
    return num_to_str(n//10)+' '+num_to_str(n%10)
    
m, n = map(int, input().split())

dic = dict()

for i in range(m, n+1):
    dic[i] = readnumber(i)
    
new_dic = dict(sorted(dic.items(), key=lambda x:x[1]))

cnt = 0
for i in new_dic.keys():
    print(i, end = ' ')
    cnt+=1
    if cnt % 10  == 0: print('')