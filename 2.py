a=[11,22,33]
# b=a #할당


#복사 방법1
import copy
c_b=copy.copy(a)
print(a,c_b)
print(id(c_b),id(a))

#복사 방법2
c_c= a[::]
print(a,c_c)
print(id(c_c),id(a))

a=[11,22,[1,2,3]]

t=a[2]
print(t,id(t),id(a[2]))
t[1]=100
a[2][1]=100
print(a,c_c)

#내가 지정한것만 바꿔줌 
#내부에 있는거까지 바꾸려면 deepcopy사용

def fun(a):
    b=a
    print(id(b))

a=[1,2,3,[1,2]]
print(id(a))
fun(a)
fun(a[::])