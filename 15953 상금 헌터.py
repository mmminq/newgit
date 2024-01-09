#15953

n = int(input())

cf1 = [5000000, 3000000, 2000000, 500000, 300000, 100000]
cf2 = [5120000, 2560000, 1280000, 640000, 320000]
    
cf1_reward = [0]
cf2_reward = [0]
    
for i in range(1,7):
    for _ in range(0, i):
        cf1_reward.append(cf1[i-1])
for i in range(0, 5):
    for _ in range(0, 2**i):
        cf2_reward.append(cf2[i])
        
for _ in range(n):
    a, b = map(int, input().split())
    if a>21 and b<32:
        print(cf2_reward[b])
    elif a<22 and b>31:
        print(cf1_reward[a])
    elif a>21 and b>31:
        print(0)
    else:
        print(cf1_reward[a]+cf2_reward[b])