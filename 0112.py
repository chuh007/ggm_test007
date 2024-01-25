# color=['red','green','blue','black','white']
# print(color[0])
# print(color[4])
# print(color[1:4])



# num=list(range(1,21,2))
# print(num)
# print(num[3:7])



# colors=['빨간색','파란색','노란색','검정색','초록색',]
# for color in colors:
#     print('나는 %s을 좋아합니다.'% color)



# animals=['사자','호랑이','사슴','곰',]
# i=0
# while i<len(animals):
#     print(animals[i])
#     i+=1



# flower=['무궁화','장미','개나리',]
# print(flower)
# flower.append('벛꽃')
# print(flower)



# scores=[]
# while True:
#    score= int(input('성적을 입력하세요(종료 시 -1 입력):'))
#    if score==-1:
#       break
#    else:
#       scores.append(score)
# print(scores)



# person1=['kim','24','kim@naver.com']
# person2=['lee','35','lee@hanmail.com']
# person=person1+person2
# print(person)



# member=['안지영',20,'경기도 김포시','jiwoang@codingschool.info',\
#         '123-1234-5678']
# print(member)
# member.remove(20)
# print(member)                 #집에서 해온거



# numbers=[[10,20,30],[40,50,60,70,80]]
# print(numbers[0][0])
# print(numbers[0][1])
# print(numbers[0][2])
# print(numbers[1][0])
# print(numbers[1][1])
# print(numbers[1][2])
# print(numbers[1][3])
# print(numbers[1][4])


# numbers=[[10,20,30],[40,50,60,70,80]]
# for i in range(len(numbers)):
#     for j in range(len(numbers[i])):
#         print('numbers[%d][%d]=%d'%(i,j,numbers[i][j]))


# scores=[[75,83,90],[86,86,73],[76,95,83],[89,96,69],[89,76,93]]
# for i in range(len(scores)):
#     sum=0
#     for j in range(len(scores[i])):
#         sum=sum+scores[i][j]
#     avg=sum/len(scores[i])
#     print('%d번째 학생의 합계:%d, 평균:%.2f'%(i+1,sum,avg))


# st=[['잠자리','풍뎅이','여치',],['짜장면','파스타','피자','국수']]
# i=0
# for s in st:
#     for t in s:
#         for u in t:
#             print(u)


# score=[64,89,100,85,77,58,79,67,96,87,\
#        87,36,82,98,84,76,63,69,53,22]
# count_su=0
# count_woo=0
# count_mi=0
# count_yang=0
# count_ga=0
# i=0
# while i<len(score):
#     if score[i]>=90 and score[i]<=100:
#         count_su+=1
#     if score[i]>=80 and score[i]<=89:
#         count_woo+=1
#     if score[i]>=70 and score[i]<=79:
#         count_mi+=1
#     if score[i]>=60 and score[i]<=69:
#         count_yang+=1
#     if score[i]>=0 and score[i]<=59:
#         count_ga+=1
#     i+=1
# print('수:%d명'%count_su)
# print('우:%d명'%count_woo)
# print('미:%d명'%count_mi)
# print('양:%d명'%count_yang)
# print('가:%d명'%count_ga)


# seats=[[0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [1,1,1,0,0,0,0,0,1,0],
#     [0,0,0,0,0,1,0,0,0,0],
#     [0,1,0,0,0,1,0,1,0,0],
#     [0,0,0,0,0,0,1,0,0,0],
#     [1,0,1,0,0,0,0,0,0,1]]
# for i in range(len(seats)):
#     for j in range(len(seats[i])):
#         if seats[i][j]==0:
#             print('%3s'%'□',end='')
#         else:
#             print('%3s'%'■',end='')
#     print()


# quest=['tr_in','b_s','_axi','air_land']
# answer=['a','u','t','p',]
# for i in range(len(quest)):
#     q='%s 에서 밑줄(_) 안에 들어갈 알파벳은?'%quest[i]
#     ans=input(q)
#     if ans==answer[i]:
#         print('정답입니다!')
#     else:
#         print('틀렸습니다!')