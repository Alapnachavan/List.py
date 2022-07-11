a=[1,"vaishu",2,"abc",2.1,3,"harshu",1.1]
i=0
b=[]
while i<len(a):
    if type (a[i])==float:
        b.append(a[i])
    i=i+1
print(b)

a=[1,5,7,"alpana",5.6,5j]
i=0
b=[]
while i<len(a):
    if type (a[i])==int:
        b.append(a[i])
    i=i+1
print(b)