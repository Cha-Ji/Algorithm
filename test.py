import collections
ct = collections.Counter()
with open('test.txt','r') as f:
    for li in f:
        ct.update(li.rstrip())

for item,cnt in ct.most_common():
    print("%s : %d"%(item,cnt))
print(ct.most_common())
