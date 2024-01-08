#6550 

#문제에서 종료 조건을 지정하지 않은 경우 try, except 구문 기억하기!

while True:
    try:
        s, t = input().split()
        s_index = 0
        s_copy = []
        
        for i in t:
            if i == s[s_index]:
                s_copy.append(i)
                s_index += 1
            if s_index == len(s):
                break
                
        if list(s) == s_copy:
            print('Yes')
        else:
            print('No')
    except:
        break