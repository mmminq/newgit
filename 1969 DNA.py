#1969

n, m = map(int, input().split())
dna = [input() for _ in range(n)]
arr = [[] for _ in range(m)]
hd = []

for i in range(m):
    dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(n):
        dic[dna[j][i]] += 1
    dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)
    hd.append(dic[0][0])
    
hd_cnt = 0
for i in range(n):
    for j in range(m):
        if hd[j] != dna[i][j]: hd_cnt += 1
for i in hd:
    print(i, end='')
print()
print(hd_cnt)