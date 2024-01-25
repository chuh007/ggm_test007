# def isPN(num):
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


# def matchWord(in_word,answer):
#     if in_word==answer:
#         msg='참 잘했어요'
#     else:
#         msg='틀렸습니다'
#     return msg

# eng_dict={'apple':'사과','lion':'사자','book':'책','love':'사랑',\
#           'friend':'친구'}
# for i in eng_dict:
#     string=input(eng_dict[i]+'에 맞는 영어 단어는? ')
#     result=matchWord(string,i)
#     print(result)


# file=open('sample.txt','w')
# file.write('안녕하세요. 반갑습니다.')
# file.close()
# print('sample.txt 파일 쓰기 완료!')


# mydic={}
# for i in range(5):
#     a=input('단어를 입력하세요: ')
#     b=input('뜻을 입력하세요: ')
#     mydic[a]=b
# print(mydic)


# scores=['안소영 97 80 93 97 93',
#         '정예린 86 100 93 86 90',
#         '김세린 91 88 99 79 92',
#         '연수정 86 100 93 89 92',
#         '박지아 80 100 95 89 90']
# data=''
# for item in scores:
#     data=data+item+'\n'
# print(data)
# file=open('scores.txt','w')
# file.write(data)
# file.close()


# file=open('scores.txt','r')
# lines=file.readlines()
# print(lines)
# for line in lines:
#     print(line,end='')
# file.close()


# file=open('scores.txt','r')
# lines=file.readlines()
# file.close()
# print(lines)
# print('-'*50)
# for line in lines:
#     student=line.split()
#     i=0
#     sum=0
#     while i<6:
#         if i==0:
#             print(student[i])
#         else:
#             sum=sum+int(student[i])
#         i+=1
#     print('합계:%d,평균:%.2f'%(sum,sum/5))
#     print('-'*50)


# def sum(numbers):
#     total=0
#     for number in numbers:
#         total+=number
#     return total

# num=(7,12,38,24,25,-7)
# print(num)
# print(sum(num))


# def strReverse(string):
#     r_string=''
#     index=len(string)
#     while index>0:
#         r_string=r_string+string[index-1]
#         index-=1
#     return r_string
# in_string=input('문자열을 입력하세요: ')
# print(strReverse(in_string))


# def numSquare(num):
#     list_new=[]
#     for i in range(1,n+1):
#         list_new.append(i**2)
#     return list_new
# n=int(input('N 값을 입력하세요: '))
# num_list=numSquare(n)
# print(num_list)


# def isVald(p):
#     if len(p)<10:
#         return False
#     is_num=False
#     is_upper=False
#     for ch in p:
#         if ch >='A'and ch <='Z':
#             is_upper=True
#         if ch >='0'and ch<='9':
#             is_num=True
#     return is_upper and is_num

# print('※ 비밀번호는 10자리 이상, 영문 대문자를 포함해야 합니다')
# password1=input('비밀번호: ')
# password2=input('비밀번호 확인: ')
# while True:
#     if isVald(password1) and password1==password2:
#         break
#     else:
#         # if not password1!=password2:
#         if not isVald(password1):
#             print('비밀번호가 잘못되었습니다! 다시 입력해주세요.')
#         else:
#             print('비밀번호와 비밀번호 확인이 일치하지 않습니다! 다시 입력하세요')
#     password1=input('비밀번호: ')
#     password2=input('비밀번호 확인: ')
# print('유효한 비밀번호 입니다.')