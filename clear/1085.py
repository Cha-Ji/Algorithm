#Ex_1085
# math
x,y,w,h=list(map(int,input().split(" ")))
min=x
if(min>y):min=y
if(min>w-x):min=w-x
if(min>h-y):min=h-y
print(min)