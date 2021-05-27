# # 삼각형의 넓이
# print("삼각형의 넓이 구하기")
# height = int(input("높이 : "))
# base = int(input("밑변 : "))
# result = (height * base) /2
# print(result)

# # 원의 넓이
# import math
# print("원의 넓이 구하기")
# radius = int(input("반지름 : "))
# result = pow(radius,2)*math.pi
# print(result)

# # 사다리꼴의 면적
# print("사다리꼴의 면적 구하기")
# low_side = int(input("밑변 : "))
# high_side = int(input("윗변 : "))
# height = int(input("높이 : "))
# result = (low_side+high_side)*height/2
# print(result)

# # cm => inch 변환
# print("cm => inch 변환하기")
# cm_value = float(input("cm 값 : "))
# inch = cm_value * 2.54
# print(inch,"inch")

# # kg => lb 변환
# print("kg => lb 변환하기")
# kg_value = float(input("변환할 kg 값 : "))
# lb = kg_value * 2.2046
# print(lb,"lb")

# # F => C 변환
# print("화씨 => 섭씨 변환하기")
# F = float(input("변환할 F : "))
# C = (F-32)*5/9
# print("섭씨 ",C,"도")

# # 거스름돈 계산하기
# print("거스름돈 계산하기")
# cost = int(input("상품의 가격 : "))
# item_count = int(input("상품의 갯수 : "))
# paid = int(input("지불한 금액 : "))
# change = paid - (cost*item_count)
# print(change,"원")

# # 평행사변형 면적 구하기
# print("평행사변형 면적 구하기")
# base = int(input("밑변 : "))
# height = int(input("높이 : "))
# result = base * height
# print(result)

# # mile => km
# print("mile => km")
# mile = float(input("변환할 mile 값 : "))
# km = mile * 1.609344
# print(km)

num = 1.2
if type(num)==float:
    print("float")
else:print("error")
