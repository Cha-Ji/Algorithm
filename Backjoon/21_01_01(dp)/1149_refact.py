d =[0]*3
for _ in range(int(input())):
    R=list(map(int,input().split()))
    d=[min(d[1],d[2])+R[0],min(d[0],d[2])+R[1],min(d[0],d[1])+R[2]]
print(min(d))