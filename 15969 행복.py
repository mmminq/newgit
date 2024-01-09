#15969

n = int(input())

score = list(map(int, input().split()))

score.sort(reverse=True)

print(score[0]-score[-1])