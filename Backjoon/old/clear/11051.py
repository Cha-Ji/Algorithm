# Ex_11051
# 이향계수
n=input().split()
i=0
x=1
y=1
while i<int(n[1]):
    x*=(int(n[0])-i)
    y*=(int(n[1])-i)
    i+=1
print(x//y%10007)