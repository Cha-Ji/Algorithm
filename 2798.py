#Ex_2798
# 블랙잭
N,M=map(int,input().split(" "))
card=list(map(int,input().split(" ")))
answer=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            temp=card[i]+card[j]+card[k]
            if(temp==M):
                answer=temp
                break
            elif(answer<temp<M):
                answer=temp
print(answer)