#Ex_2869
#math
A,B,V=list(map(int,input().split(" ")))
LastDay=V-A
OneDay=A-B
result=LastDay//OneDay+1
if(LastDay%OneDay>0):
    print(result+1)
else:print(result)