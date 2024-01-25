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


# maban=[['개','똥','아'],['똥','쌌','니'],['아','니','오']]
# for i in range(len(maban)):
#     sum=0
#     for j in range(len(maban[i])):
#         sum=maban[i][j]
#         print(sum,end='')
#     print()


# maban=[['개','똥','아'],['똥1','쌌','니'],['아1','니1','오']]
# for i in range(len(maban)):
#     sum=0
#     for j in range(len(maban[i])):
#         sum=maban[j][i]
#         print(sum,end='')
#     print()


# a='1'
# z=1
# for i in range(5):
#     print('%s%s'%(' '*(5-i),a))
#     i+=1
#     z+=1
#     a='%s'%z+a


# avengers=('캡.아','아이언맨','헐크','토르','닥.스')
# i=0
# while i<len(avengers):
#     print(avengers[i])
#     i+=1


# avengers=('캡.아','아이언맨','헐크','토르','닥.스')
# a=0
# z=[]
# for p in range(5):
#     z.append(avengers[a])
#     a+=1
# z.remove('아이언맨')
# print(z)


# menu={'짜장면':5000,'짬뽕':6000,'볶음밥':7000}
# a=input('음식 이름을 넣으세요: ')
# print(menu[a])


# menu={'짜장면':5000,'짬뽕':6000,'볶음밥':7000}
# p=0
# while True:
#     a=input('주문할 음식 이름을 넣으세요: ')
#     i=int(input('몇개 주문하시겠습니까? '))
#     p+=menu[a]*i
#     yn=input('더 주문 하시겠습니까? ')
#     if yn=='ㄴ':
#         break
# print(p)