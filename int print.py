# a=["laddu",23,24,"yes",53,4]
# a=["aarti",12,"vaishu","sona",87,98,"mona",78,99,902]
# i=0
# string=0
# num=0
# c=[]
# d=[]
# while i<len(a):
#     if type(a[i])==str:
#         string=string+1
#         c.append(a[i])   
#     else:
#         num=num+1
#         d.append(a[i])
#     i=i+1
# print("string",string,c)
# print("num",num,d)

a=["aarti",12,"vaishu","sona",87,98,"mona",78,99,902]
i=0
string=0
num=0
b=[]
c=[]
while i<len(a):
    if type (a[i])==str:
        string=string+1
        b.append(a[i])
    else:
        num=num+1
        c.append(a[i])
    i=i+1
print("string",string,b)
print("num",num,c)


i=0
num=0
string=0
b=[]
c=[]
while i<len(a):
    if type (a[i])==str:
        string=string+1
        b.append(a[i])
    else:
        num=num+1
        c.append(a[i])
    i=i+1
print()



