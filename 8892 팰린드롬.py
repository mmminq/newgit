case = int(input())

for i in range(case):
    n = int(input())
    word = []
    for i in range(n):
        w = input()
        word.append(w)
        
    breaker = 0
    checker = 0
    for i in range(len(word)-1):
        for j in range(i+1, len(word)):
            n_word = word[i] + word[j]
            if n_word == n_word[::-1]:
                print(n_word)
                breaker = 1
                checker = 1
                break
            n_word = word[j] + word[i]
            if n_word == n_word[::-1]:
                print(n_word)
                breaker = 1
                checker = 1
                break
        if breaker == 1:
            break
    
    if checker == 0:
        print(0)