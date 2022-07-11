a=["Alpana","Dhananjay","Chavan"]
i=0
b=[]
c=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        # if a[i][j]>="A" and a[i][j]<="Z" or a[i][j]>="a" and a[i][j]<="z":
            b.append(a[i][j])
        # else:
        #     c.append(a[i][j])
        j=j+1
    i=i+1
print(b)
# print(c)

        