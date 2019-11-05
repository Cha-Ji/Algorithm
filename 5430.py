#Ex_5430
# 덱
# pop(0)의 효율적인 방법


import sys

for _ in range(int(sys.stdin.readline())):
    AC=[]
    err=1
    rev=True

    p=sys.stdin.readline()
    n=int(sys.stdin.readline())
    x=sys.stdin.readline()[1:-2].split(',')

    front=0
    rear=n-1

    for i in range(n):
        AC.append(x[i])

    for j in range(len(p)-1):

        if(p[j]=='R'):
            rev = not rev
        elif(p[j]=='D'):
            if rev==True:
                front+=1
            else:
                rear-=1

    if(front>rear+1):sys.stdout.write("error\n")

    else:

        sys.stdout.write("[")

        if(rev==False):
            k=rear
            while k>front:
                sys.stdout.write(AC[k]+',')
                k-=1
            if(rear>=front):
                sys.stdout.write(AC[front])

        else:
            k=front
            while k<rear:
                sys.stdout.write(AC[k]+',')
                k+=1
            if(rear>=front):
                sys.stdout.write(AC[rear])

        sys.stdout.write(']\n')