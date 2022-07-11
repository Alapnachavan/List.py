# a=[1,2,[3,4,5],6,9,[2,9]]



# a=[1,2,[3,4,5],6,9,[2,9]]
# sum=0
# d=m[k]
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       sum=sum+0
#       k=k+1
#             j=j+1
#     i=i+1
# print(sum)


# i=0
# sum=0
# a=0
# while i<len(a):
#     j=0
#     sum1=0
#     while j<len(a[0:1]):
#         sum1=sum1+[i][j]
        # j=j+1
    # i=i+1
    # sum=sum1+sum
# print(sum)


# a=[[1,2,0],[3,2,5],[5,2,9]]
# i=0
# largest=a[0]
# while i<len(a):
#     if a[i]>largest:

#         largest=a[i]
#     i=i+1
# print(largest)


a=[[1,2,3,4],[2,4,56,],[6,9,8,6]]
i=0
sum=0
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
    i=i+1
print(sum)