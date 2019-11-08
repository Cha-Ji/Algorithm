#Ex_6064
# math
for _ in range(int(input())):
    M,N,x,y=list(map(int,input().split(" ")))
    result=x
    check=0
    while result<=M*N:
        if((result-y)%N==0):
            print(result)
            check=1
            break
        result+=M
    if(check==0):print(-1)