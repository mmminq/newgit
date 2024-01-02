#1699 블로그 참고
#작은 문제부터 해결하는 bottom up 방식의 Dynamic Programming 문제

n = int(input())
dp = [i for i in range(n+1)] # index 관리의 편의성을 위해 0~n까지 리스트 초기화

for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j] + 1: # ex) dp[15] > dp[15-3*3] + 1이므로
            dp[i] = dp[i-j*j] + 1 # dp[15] = dp[6] + 1 = (dp[4] + dp[2] + 1) + 1
            
print(dp[n])