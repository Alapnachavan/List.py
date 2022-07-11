# a=[3678,2346,6554,1234,7]
# i=0
# # b=[]
# while i<len(a):
#     if type(a[i])==int:
#         j=0
#         sum=0
#         while j<4:
#             sum=sum+a[i][j]
#         j=j+1
#     i=i+1
# print(sum)

# a=[1,23,[12,3],5,[2,3,4],43,5]
# i=0
# sum=0
# # b=[]
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         while i<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)
# b.append(sum)
# print(b)

a=[1,23,[12,3],5,[2,3,4],43,5]
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j=j+1
    else:
        b.append(a[i])
    i=i+1
print(b)

# a=[1,12,34,[45,67],3,4,[4,5]]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j=j+1
#     else:
#         b.append(a[i])
#         i=+1
# print(b)


