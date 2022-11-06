a=[1,2,3,4]
b=['s','f','g']
c=[11,22,'ee']
a.extend(b)
a.extend(c)
print(a)

mylist = []
for x in range(max(len(a), len(b))):
    if x < len(a):
        mylist.append(a[x])
    if x < len(b):
        mylist.append(b[x])
        
    print(mylist)
