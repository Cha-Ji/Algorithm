#Ex_1002
# math
for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2=list(map(int,input().split(" ")))
    d=((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    r=(r2+r1)*(r2+r1)
    #원 일치
    if(r1==r2 and d==0):print(-1)
    #원 외접
    elif(r==d):print(1)
    #원 내접
    elif((r2-r1)*(r2-r1)==d):print(1)
    #원 떨어져
    elif(d>r):print(0)
    #원 안에 미니원
    elif((r2-r1)*(r2-r1)>d):print(0)
    else:print(2)