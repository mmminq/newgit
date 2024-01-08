#4659

def check(pw):
    #condition 1
    if ('a' not in pw) and ('e' not in pw) and ('i' not in pw) and ('o' not in pw) and ('u' not in pw):
        return 'not acceptable.'
    #condition 2
    for i in range(len(pw)-2):
        if (pw[i] not in vowel) and (pw[i+1] not in vowel) and (pw[i+2] not in vowel):
            return 'not acceptable.'
        elif (pw[i] in vowel) and (pw[i+1] in vowel) and (pw[i+2] in vowel):
            return 'not acceptable.'
    #condition 3
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1]:
            if pw[i] == 'e' or pw[i] == 'o':
                continue
            else:
                return 'not acceptable.'
    return 'acceptable.'

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    pw = input()
    if pw == 'end':
        break
    
    print('<'+pw+'> is '+check(pw))