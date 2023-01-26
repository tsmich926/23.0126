#과제6-3
#문자열을 전달 받아 문자열의 모음갯수를 반환하는 count_vowels함수
# s=input()
# def count_vowels:
vowels=['a','e','i','o','u']
count=0
s=input()
for i in s:
    for vo in vowels:
        if i == vo :
            count=count+1

print(count)


def count_vowels:
    vowels=['a','e','i','o','u']
    count=0
    s=input()
    for i in s:
    for vo in vowels:
        if i == vo :
            count=count+1
return count 

print(count)

#단어를 입력받아서 모음의 개수를 리턴
def count_vowels(word):
    cnt=0
    vowels='aeiou'
    for w in word:
        if w in vowels:
            cnt +=1
    return cnt

''.c
for w in vowels:
    cnt+= word.count(w)