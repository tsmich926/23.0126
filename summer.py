
#? set
# 인덱스를 통한 접근 불가(순서가 없으므로) 
# 집합
#! 중괄호 사용-딕셔너리는 키:밸류 형태로 이뤄짐
# a={'사과','수박','배'}
# a.add('딸기') 
# print(a) #순서를 보장하지 않으므로 출력 순서 바뀔수 있음.
# a.update('배','참외') #여러개 추가
#! a.pop()  제거와 반환을 함께한다.
# x=a.pop()
# print(x)

#? 딕셔너리
# data=[['ㅇㅇ':21],['ㄴㄴ':8]]
# for each in data:
#     if each[0]=='ㄴㄴ':
#         print(each[1])

# data={'dd':15,'sd':20,'ddd':77}
#! data['dd'] 
#찾고자하는 데이터를 바로 찾을 수 있다.
#key는 변경불가능한 데이터만 활용가능
#! d.get(key) 키의 값을 반환,키가 딕셔너리에 없을 경우 None을 반환
#! d[key]를 했을 때 키가 딕안에 없으면 에러가 난다.


#주어진 리스트의 4번째 자리에 있는 항목을 제거하고 변수에 할당해 주세요
sample_list=[11,22,33,55,66]

print(sample_list[3])
ele=sample_list.pop(3)
print(ele)

#샘플 리스트의 가장 뒤에 44를 추가
sample_list.append(44)
print(sample_list)

#할당해놓은 변수값을 샘플리스트의 2번 인덱스에 추가
sample_list.insert(2,ele)
print(sample_list)

#?튜플
#주어진 튜플에서 44와 55의 값을 새로운 튜플에 할당
my_tuple=(11,22,33,44,55,66)
New_tuple=my_tuple[3:5] #New_tuple=my_tuple[3:-1]과 같다.
print(New_tuple)

#복사방법
#?할당
orlist=[1,2,3]
copy_list=orlist
print(copy_list,orlist)
copy_list[0]='hello'
print(copy_list,orlist) #대입연산자 =을 통한 복사는 객체에 대한 객체참조(주소값)를 복사
# [1, 2, 3] [1, 2, 3]
# ['hello', 2, 3] ['hello', 2, 3] 결과값


#? 깊은 복사
# 메모리 다른공간에 데이터를 복사해서 다른곳을 가르키게 한다.
# 복사한 데이터 변경해도 원본 데이터는 변하지 않는다.
a=[1,2,['a','b']]
import copy
copy,deepcopy(a)
print(a,b) #[1,2,['a','b']] [1,2,['a','b']]
b[2][0]=0 
print(a,b) #[1,2,['a','b']] [1,2,['0','b']]
#참조되는 것까지 복사가 된다


#? 얕은 복사
slice연산자를 활용할 수 있다.
연산된 결과를 (다른주소)에 복사
a=[1,2,3]
b=a[:]
print(a,b)
b[0]=5
print(a,b)
# [1, 2, 3] [1, 2, 3]
# [1, 2, 3] [5, 2, 3] 결과

#?깊은복사와 얕은 복사 구분
#대입연산자를 활용하면 얕은 복사
# 슬라이싱 사용
# copy.copy 1차원적으로 다른 메모리에 복사해주는 메소드



#뒤에 있는 값을 기준으로 정렬하려면
#함수사용
scores =[('korea',77),('math',44)]

def check(x):
    return x[1]

scores.sort(key=check)
print(scores)

#람다함수사용
scores.sort(key=lamda x:x[1])
print(scores)
