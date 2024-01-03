# 13413

n = int(input())
diff_arr = [] # 바꿔야 하는 말을 append할 리스트
cnt_arr = [] # 변경 횟수를 append할 리스트
for _ in range(n):
    m = int(input())
    a = input()
    b = input()
    for i in range(m):
        if a[i] != b[i]:
            diff_arr.append(a[i])
    if diff_arr.count('W') > diff_arr.count('B'):
        cnt_arr.append(diff_arr.count('W'))
    else:
        cnt_arr.append(diff_arr.count('B'))
    diff_arr = []
        
for i in cnt_arr:
    print(i)