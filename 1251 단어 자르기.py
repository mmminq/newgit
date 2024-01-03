#1251 시도는 좋았으나 방법이 틀림, 특정 케이스를 구하는 것이 아니라 모든 케이스를 계산해야 함

"""word = list(map(str, input()))
new_word = []
for _ in range(2):
    sorted_word = sorted(word) #알파벳 순 오름차순 정렬한 리스트
    first_index = word.index(sorted_word[0]) # word 리스트에서 가장 빠른 알파벳의 인덱스
    temp = word[0:first_index+1] # new_word 리스트에 역순으로 추가
    temp.reverse()
    new_word.append(temp)
    del word[0:first_index+1] # new_word 리스트에 역순으로 추가
word.reverse() # 남은 word를 모두 new_word에 추가
new_word.append(word)

for i in new_word:
    for j in i:
        print(j, end = '')"""
        
###################################################################################

#블로그 참고

word = list(map(str, input()))
words = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        #단어를 세 덩어리로 쪼갠다.
        first = word[:i]
        second = word[i:j]
        third = word[j:]
        
        #각 덩어리를 뒤집는다.
        first.reverse()
        second.reverse()
        third.reverse()
    
        #뒤집은 덩어리를 합쳐서 리스트에 추가한다.
        words.append("".join(first+second+third))
        
#오름차순으로 가장 빠른 단어를 출력한다.
print(min(words))
