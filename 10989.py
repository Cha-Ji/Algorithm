#Ex_10989
# sort
# memory
#Ex_2751
# python sort
import sys
sample=[0]*10001

for _ in range(int(input())):
    a=int(sys.stdin.readline())
    sample[a]=sample[a]+1

for i in range(len(sample)):
    if sample[i]!=0:
        for _ in range(sample[i]):
            print(i)