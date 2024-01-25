# def say_hallo(name):
#     print('%s님 안녕하세요'%name)
# say_hallo('김지수')
# say_hallo('최진영')
# say_hallo('이예린')


# def even_odd(n):
#     if n%2==0:
#         print('%d->짝수'%n)
#     else:
#         print('%d->홀수'%n)
# even_odd(15)
# even_odd(26)


# def inch_to_cm(inch):
#     cm=inch*2.54
#     return cm
# num=int(input('인치를 입력하세요: '))
# result=inch_to_cm(num)
# print('%d inch=>%.2f cm'%(num,result))


# def besu5(n):
#     if n%5==0:
#         rel=True
#     else:
#         rel=False
#     return rel
# num=int(input('양의 정수를 입력하세요: '))
# result=besu5(num)
# if result==True:
#     print('%d->5의 배수이다'%num)
# else:
#     print('%d->5의 배수가 아니다'%num)


# def cmg(x,y):
#     if x>y:
#         small=y
#     else:
#         small=x
#     for i in range(1,small+1):
#         if((x%i==0)and(y%i==0)):
#             result=i
#     return result

# num1=int(input('첫번째 수를 입력하세요: '))
# num2=int(input('두번째 수를 입력하세요: '))
# mg=cmg(num1,num2)
# print('%d와 %d의 최대공약수: %d'%(num1,num2,mg))


#학원

# twice=['나연','정연','모모','사나','지효','미나','다현','채영','쯔위']
# print(twice)


# menulist=[]
# menulist.append('아메리카노')
# menulist.append('카페라떼')
# menulist.append('카페모카')
# menulist.remove('카페라떼')
# print(menulist)


# whshlist=[]
# i=0
# while i <3:
#     a=input('소원을 입력하세요: ')
#     whshlist.append(a)
#     i+=1
# print(whshlist)


# a=['alpha','brawo','charilie','delta','echo','foxtrot','golf','hotel','india']
# b=[]
# for i in a:
#     if len(i)==5:
#         b.append(i)
# print(b)


# ans=['o','x','o','x','o','o','x','o','x','o']
# s=0
# a=0
# for i in ans:
#     if i=='o':
#         if a>4:
#             s+=12
#         else:
#             s+=8
#     a+=1
# print(s)


# likelist=[]
# while len(likelist)<5:
#     a=input('항목을 입력하세요: ')
#     yn=input('추가할까요? 삭제할까요?')
#     if yn=='추가':
#         likelist.append(a)
#     else:
#         likelist.remove(a)
# print(likelist)


# menw=['짜장면','우동','짬뽕','볶음밥']
# print(menw)
# menw[1]='사천탕면'
# print(menw)
# menw[0]='쟁반짜장면'
# menw[3]='삼선볶음밥'
# menw[2]='해물짬뽕'
# print(menw)


# last_day=[31,28,31,30,31,30,31,31,30,31,30,31]
# a=0
# for i in last_day:
#     a+=i
# print(a)


# last_day=[31,28,31,30,31,30,31,31,30,31,30,31]
# a=int(input('월의 말일을 입력하세요: '))
# print(last_day[a-1])


# nums=[3,21,35,57,24,82,8]
# a=0
# for i in nums:
#     i+=10
#     nums[a]=i
#     a+=1
# print(nums)


# scores=[[89,83,91],[77,98,95]]
# a=[]
# for i in range(len(scores)):
#     sum=0
#     for j in range(len(scores[i])):
#         sum=sum+scores[i][j]
#     a.append(sum)
# q=a[0]
# w=a[1]
# if q<w:
#     print('2번 학생이 더 높다')
# else:
#     print('1번 학생이 더 높다')