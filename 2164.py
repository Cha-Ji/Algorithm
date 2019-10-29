#Ex_2164
#큐
n=int(input())
q=[]
head=-1
rear=n-1
for _ in range(n):
    q.append(_+1)
while rear-head>2:
    head+=2
    q.append(q[head])
    rear+=1
if(n-head==2):
    print(q[rear-1])
else:
    print(q[rear])