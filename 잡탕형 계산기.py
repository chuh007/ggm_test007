# a=1         #팩토리얼 입력한 값까지 출력
# z=1
# i=int(input('수 입력: '))+1
# while a<i:
#     z=a*z
#     print('%d!=%d'%(a,z))
#     a+=1



# n1= int(input('시작 숫자를 입력하세요: '))           #시작 수 부터 끝 숫자까지의 합 출력
# n2= int(input('끝 숫자를 입력하세요: '))
# z=0
# for a in range(n1,n2+1):
#     z=a+z
# print('%d부터 %d 까지의 합계는 %d 입니다.'%(n1,n2,z))



# def isPN(num):            #N값 까지의 소수를 전부 출력
#     prime_yes=True
#     for i in range(2,a):
#         if a %i==0:
#             prime_yes=False
#             break
#     return prime_yes
# z=0
# n= int(input('N값을 입력해 주세요: '))
# print('2~%d까지의 정수 중 소수: '%n,end='')
# for a in range(2,n+1):
#     is_prime=isPN(a)
#     if is_prime:
#         print(a,end=' ')
#         z+=1
# print()
# print('소수의 개수: %d'%z)


# def numSquare(num):          #제곱 입력값까지 출력
#     list_new=[]
#     for i in range(1,n+1):
#         list_new.append(i**2)
#     return list_new
# n=int(input('N 값을 입력하세요: '))
# num_list=numSquare(n)
# print(num_list)