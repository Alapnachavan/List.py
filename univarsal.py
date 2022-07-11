l=[7,9,5,3,8]
i=len(l)-1
b=[]
max=0
while i>=0:
    if l[i]>max:
        max=l[i]
        a=i
        b.insert(0,a)
    i-=1
print(b)