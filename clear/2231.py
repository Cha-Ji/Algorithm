#Ex_2231
# brute force
# 분해합
target_num=int(input())
for i in range(target_num+1):
    decom=map(int,str(i))
    if i+sum(decom)==target_num:
        print(i)
        break
    if i==target_num:
        print(0)