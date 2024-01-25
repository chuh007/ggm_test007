# sen=input('문장을 입력해 주세요: ')
# i=len(sen)-1
# while i >=0:
#     if sen[i]==' ':
#         print('-',end='')
#     else:
#         print('%s'%sen[i],end='')
#     i-=1

# count=0
# a=1
# while a<101:
#     if a%3!=0 and a%5!=0:
#         print(a,end=" ")
#         count+=1
#         if count%10==0:
#             print()
#     a=a+1

# a= input('수를 입력하시오: ')
# i= int(a)
# while i>=0:
#     for z in range(1,i):
#         # if i%z==0:
#             # print(i)
#             print(z)
#     # i-=1


# i = 13
# # 2-24

# num = 5000

# for i in range(2, num+1):
#     prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             prime = False

#     if prime == True:
#         print(i, '소수')

            # print(j)
# for 문
# # b=1
# # i=int(input('수 입력: '))
# # for a in range(1,i+1):
# #     b=a*b
# #     print('%d!=%d'%(a,b))

# a=1
# z=1
# i=int(input('수 입력: '))+1
# while a<i:
#     z=a*z
#     print('%d!=%d'%(a,z))
#     a+=1

# print('-'*30)
# print('%3s\t%3s\t%3s\t%3s'%('cm','mm','m','inch'))
# print('-'*30)
# for cm in range(10,81,5):
#     mm=cm*10
#     m=cm/100
#     inch=cm*0.3937
#     print('%3.0f\t%3.0f\t%3.2f\t%3.2f\t'%(cm,mm,m,inch))
# print('-'*30)

# print('-'*30)
# print('%3s\t%3s\t%3s\t%3s'%('cm','mm','m','inch'))
# print('-'*30)
# cm=10
# while cm <=80:
#     mm=cm*10
#     m=cm/100
#     inch=cm*0.3937
#     print('%3.0f\t%3.0f\t%3.2f\t%3.2f\t'%(cm,mm,m,inch))
#     cm+=5


# # input()  했을 때 q 를 누르면 바로 종료하는 상황

# while True:
#     a = input('?')
#     if a == 'q':
#         break
#     print(a)

# z=True
# while z==True:
#     a= int(input('성적을 입력하세요: '))
#     if a>=90:
#         print('등급: 수')
#     elif a>=80:
#         print('등급: 우')
#     elif a>=70:
#         print('등급: 미')
#     elif a>=60:
#         print('등급: 양')
#     else:
#         print('등급: 가')
#     z=False
#     qy=input(('계속하시겠습니까?(중단:q, 계속:y) '))
#     if qy=='y':
#         z=True

# n=int(input('구구단 단을 입력하시오: '))
# for a in range(1,10):
#     print('%dX%d=%d'%(n,a,n*a))

# a=True
# while a==True:
#     text=input('내용: ')
#     print('입력한 내용: '+text)
#     if text=="종료":
#         a=False

# n1= int(input('시작숫자를 입력하세요: '))
# n2= int(input('끝숫자를 입력하세요: '))
# z=0
# for a in range(n1,n2+1):
#     z=a+z
# print('%d부터 %d 까지의 합계는 %d 입니다.'%(n1,n2,z))

# for a in range(24):
#     for b in range(60):
#         print('%d:%d'%(a,b))

# text='Life is short you need Python'
# i=0
# count_e=0
# count_i=0
# count_o=0
# while i<=len(text)-1:
#     if text[i]=='e':
#         count_e+=1
#     elif text[i]=='i':
#         count_i+=1
#     elif text[i]=='o':
#         count_o+=1
#     i+=1
# print(count_e,count_i,count_o)