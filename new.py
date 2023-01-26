#단어를 입력받아서 모음의 개수를 리턴하는 함수
def count_vowels(word):
    cnt=0
    vowels='aeiou'
    for w in word:
        if w in vowels:
            cnt +=1
    return cnt

#다른방법
''.c
for w in vowels:
    cnt+= word.count(w)
return cnt