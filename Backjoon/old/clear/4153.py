#Ex_4153
# math
while 1:
    x,y,z=list(map(int,input().split()))
    if(x==0):break
    if(x>z):
        x,z=z,x
    if(y>z):
        y,z=z,y
    print("right" if x*x+y*y==z*z else "wrong")