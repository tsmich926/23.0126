# orlist=[1,2,3]
# copy_list=orlist
# print(copy_list,orlist)
# copy_list[0]='hello'
# print(copy_list,orlist)


# a=[1,2,3]
# b=a[:]
# print(a,b)
# b[0]=5
# print(a,b)

# test_list= [12,5,8,95,2]
# test_list.sort()
# print(test_list)

#뒤에 있는 값을 기준으로 정렬하려면
# scores =[('korea',77),('math',44)]

# def check(x):
#     return x[1]

# scores.sort(key=check)
# print(scores)

#람다함수사용
# scores.sort(key=lambda x:x[1])
# print(scores)

# grain_lst=[('고구',3000),('양파',2500),('토란',450)]
# for i in grain_lst:
#     print(type(i)) #타입은 튜플

# grain_lst.sort(key=lambda x:x[1])
# print(grain_lst) #가격을 기준으로 정렬

# persons=[{'name':'fd','age':18'},{'name:hgdf','age:11'},{'name:ert','age:12'}]
# # print(persons.sort()) #에러뜸 작은값
# persons.sort(key=lambda x:x['age'])
# print(persons)

# a=[11,22,[1,2,3]]

# t=a[2]
# print(t,id(t),id(a[2]))
# t[1]=100
# a[2][1]=100
# print(a,c_c)

def fun(a):
    b=a
    print(id(b))
    b[1]=1000

a=[1,2,3,[1,2]]
print(id(a))
fun(a)
fun(a[::])