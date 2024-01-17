#1652 블로그 참고

n = int(input())
map_list = [input().strip() for _ in range(n)]

rowcnt, colcnt = 0, 0

for i in range(n):
    tmp_rowcnt, tmp_colcnt = 0, 0
    for j in range(n):
        if map_list[i][j] == '.':
            tmp_rowcnt += 1
        else:
            if tmp_rowcnt > 1: # 2 이상 연속된 경우일 때
                rowcnt += 1
            tmp_rowcnt = 0
    
        if map_list[j][i] == '.':
            tmp_colcnt += 1
        else:
            if tmp_colcnt > 1:
                colcnt += 1
            tmp_colcnt = 0
    if tmp_rowcnt > 1:
        rowcnt += 1
    if tmp_colcnt > 1:
        colcnt += 1
            
print(rowcnt, colcnt)