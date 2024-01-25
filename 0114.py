# phones={'z플립':2021,'노트 20':2020,'A03':2021,'S9':2018,}
# print(phones)
# for key in phones:
#     print('%s=>%s'%(key,phones[key]))
# print(len(phones))


# ad={'id':'admin','password':'12345'}
# in_id=input('아이디를 입력하세요: ')
# in_password=input('비밀번호를 입력하세요')
# if (in_id==ad['id'] and in_password==ad['password']):
#     print('정보에 접근 권한이 있음')
# else:
#     print('정보에 접근 권한이 없음')


# words={'꽃':'flower','나비':'butterfly','학교':'school','자동차':'car',\
#        '비행기':'airplane',}
# print('<영어 단어 맞추기 퀴즈>')
# for kor in words:
#     in_word=input('%s에 해당하는 영어 단어를 입력해 주세요: '%kor)    # %s를 %d로 잘못 써놓고 못봐서, 다 맞아놓고 30분을 썼네
#     if in_word==words[kor]:
#         print('정답입니다')
#     else:
#         print('틀렸습니다')


# admin=('rubato','12345','rubat@naver.com')
# print('-관리자 정보')
# print('아이디: '+admin[0])
# print('비밀번호: '+admin[1])
# print('이메일: '+admin[2])


# dans=(2,3,4,5,6,7,8,9)
# print('구구단표')
# print('='*50)
# for dan in dans:
#     print(str(dan)+'단')
#     for i in range(1,10):
#         print('%dx%d=%d'%(dan,i,dan*i))
#     print('-'*30)


# scores={'김채린':85,'박수정':98,'함소희':94,'안예린':90,'연수진':93}
# sum=0
# for key in scores:
#     sum=sum+scores[key]
#     print('%s:%d'%(key,scores[key]))
# avg=sum/len(scores)
# print('합계: %d, 평균: %.2f'%(sum,avg))


# def hello():
#     print('안녕하세요')
# hello()
# hello()
# hello() 