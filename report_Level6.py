# # 3의 배수 판별
# print("3의 배수 판별기")
# num = int(input("판별할 숫자 : "))
# print("3의 배수입니다!"if num%3==0 else "3의 배수가 아닙니다!")
#
# # ex_2
# print("범위에 있는지 판별하기")
# num = int(input("판별할 숫자 : "))
# if 30<num<=100:
#     print("범위 안에 있습니다!")
# else:
#     print("범위 밖에 있습니다!")
#
# # password
# print("로그인하기")
# password = 0000
# if int(input("비밀번호 : ")) ==password:
#     print("로그인 성공!")
# else:print("로그인 실패!")
#
# # 주민번호로 성별 판별하기
# print("성별 판별하기!")
# num = int(input("주민번호 뒷자리 : "))
# if num[0]>8:print("존재하지 않는 주민번호입니다.")
# else:
#     if num[0]%2==1:
#         print("남성입니다.")
#     else:print("여성입니다.")
#
# # 안경 추천하기
# print("안경 추천하기")
# vision = float(input("시력 : "))
# print("착용을 권합니다."if vision<=0.7 else "건강합니다!")
#
# # 레벨 부여하기
# print("레벨 부여하기")
# post_count = int(input("글쓰기 갯수 : "))
# comment_count = int(input("댓글 갯수 : "))
# if post_count>=5 and comment_count>=10:
#     level = 7
# else:level = 9
# print("레벨",level)

# # 사칙연산
# print("<연산하기> 1:더하기 2:빼기 3:곱하기 4:나누기")
# cal = int(input("수행할 연산 : "))
# cal_list={1:"+",2:"-",3:"*",4:"/"}
# while cal not in cal_list.keys():
#     print("1,2,3,4 중에 선택하세요")
#     cal = int(input("수행할 연산 : "))
# num1 = int(input("연산할 숫자1 : "))
# num2 = int(input("연산할 숫자2 : "))
# print(num1,cal_list[cal],num2," =",end=" ")
# if cal==1:
#     print(num1+num2)
# elif cal==2:
#     print(num1-num2)
# elif cal==3:
#     print(num1*num2)
# elif cal==4:
#     if num2==0:
#         print("연산이 불가능합니다.")
#     else:print(num1/num2)

# # 계절 판별기
# print("계절 판별하기")
# month = int(input("월 : "))
# month_list=[1,2,3,4,5,6,7,8,9,10,11,12]
# while month not in month_list:
#     month = int(input("1~12월 중 입력해주세요\n월: "))
# if month<=2 or month==12:
#     season = "겨울"
# elif month<=5:
#     seson = "봄"
# elif month<=8:
#     season = "여름"
# else:season="가을"
# print(str(month)+"월은",season+"입니다.")

# # 금액 계산하기
# print("금액 계산하기")
# cost = int(input("물건 가격 : "))
# item_count = int(input("물건 갯수 : "))
# total = cost * item_count
#
# if 30000 <= total < 50000:
#     total += 2000
# elif total < 30000:
#     total += 5000
# print("총 금액은 "+str(total)+"원 입니다.")

import collections
cont = collections.Counter(['aa','bb','cc','aa'])
cont.update('aabcd')
print(cont)
