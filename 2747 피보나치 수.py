#2747 블로그 참고

# 재귀함수 이용 시 TimeOver 발생, 단순 반복문을 사용해서 해결

n = int(input())

a, b = 0, 1

for i in range(n):
    a, b = b, a+b
    
print(a)