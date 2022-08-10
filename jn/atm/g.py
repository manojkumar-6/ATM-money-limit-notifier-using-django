from re import L


s=[1,2,3,4,5]
k=3
l=[]
for i in s:
    l.append(i)
    #print(l)
    if i>=k:
        continue
    else:
        l=[]
print(len(l))