#Ex_1018
# brute force
b=['BWBWBWBW']
w=['WBWBWBWB']
init_b=(b+w)*4

def counting(field,x,y):
    b_count=0
    w_count=0
    for i in range(8):
        for j in range(8):
            if(field[i+x][j+y] != init_b[i][j]):
                b_count+=1
            else:w_count+=1
    return b_count if b_count<w_count else w_count

N,M=map(int,input().split(" "))
field=[0]*N
for i in range(N):
    field[i]=input()

minimum=64
for i in range(0,N-7):
    for j in range(0,M-7):
        cnt=counting(field,i,j)
        minimum=cnt if cnt<minimum else minimum
print(minimum)