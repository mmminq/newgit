#2204

cases = []
while 1:
    n = int(input())
    if n == 0: break
    words = []
    low_words = []
    for i in range(n):
        word = input()
        words.append(word)
        low_words.append(word.lower())
    low_words.sort()
    first = low_words[0]
    for i in words:
        if i.lower() == first:
            cases.append(i)

for i in cases:
    print(i)
        