#Ex_3009
# math
x1,y1=list(map(int,input().split(" ")))
x2,y2=list(map(int,input().split(" ")))
x3,y3=list(map(int,input().split(" ")))
if(x1!=x3):
    if(x2!=x3):x=x3
    else:x=x1
else:x=x2
if(y1!=y3):
    if(y2!=y3):y=y3
    else:y=y1
else:y=y2
print(x,y)

