from collections import Counter

entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
                '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
                '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']


#set으로 중복제거하고 입장명단 출력하기
# en=set(entry_record)
# print(en)  
# list=[]

# ex=set(exit_record)
# print(ex)
# sorted(ex)
# print(ex)


#입장기록 출력하기
# for i in en:
#     c=entry_record.count(i)
#     print(i,c)

exit_counter=Counter(exit_record)
# print(exit_record)

entry_counter=Counter(entry_record)
# print(entry_counter)

entry_counter.subtract(exit_counter)

print(entry_counter)
new_lst= sorted(entry_counter.items(),key=lambda x:x[1], reverse=True)
print(new_lst)


#수상한 사람 뽑아내기
for i in range(len(new_lst)):
    if new_lst[i][1]>0:
        print(f'{new_lst[i][0]} 입장기록이 {new_lst[i][1]} 회 더 많아 수상함')
    elif new_lst[i][1]<0:
        print(f'{new_lst[i][0]} 입장기록이 {-new_lst[i][1]} 회 더 많아 수상함')

# new_lst= sorted(entry_counter.items(),key=lambda x:x[1], reverse=True)
# print(new_lst)
# toplst=new_lst[:3]
# print(toplst)

#탑쓰리 출력
# for i in toplst:
#     print(i)

#most_common 을 사용해 세명 출력
# print(count_entry.most_common(3))

#서브트랙트사용
# print(count_entry.subtract(count_exit))
# print(count_entry)

#서브트랙트 정보출력
# for name,cnt in count_entry.items()
#     print(name,cnt)

# nums=[2,3,4,5]
# t1=sorted(nums)
# t2=nums.sort()
# print(t1,t2)