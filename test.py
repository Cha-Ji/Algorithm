#Ex_1655
# priority Queue
# Sort
import sys
i =False
sorted_list=[0]*20001
total_count=0
for _ in range(int(sys.stdin.readline())):
    odd_list=[20001,20001]
    i=not i
    x=int(sys.stdin.readline())
    sorted_list[x+10000]+=1
    total_count+=1
    j,count,target=0,0,0
    #odd
    while count<(total_count//2)+1:
        if sorted_list[j]>0:
            if i==False:
                odd_list.pop(0)
                odd_list.append(j)
            count+=sorted_list[j]
        j+=1

    if (total_count//2)+1==count and i==False:
        target=odd_list[0 + (odd_list[0]>odd_list[1])]
    else: target=j-1
    print(target-10000)


