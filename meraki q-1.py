numbers=[50, 40, 23, 22,21,70, 56, 12, 5, 10, 7]
i=0
a=[]
count=0
while i< len(numbers):
    if numbers[i]>=20 and numbers[i]<=40:
        a.append(numbers[i])
        count=count+1
    i=i+1
print(count)
print(a)                                                                                                               
#  


# write a code ,that count the numbers between 20 and 40 and them print its count
# numbers=[50,40,23,70,56,12,5,10,7]
# i=0
# while i<len(numbers):
#     if numbers[i]>20 and numbers[i]<=40:
#         print(numbers[i],"its count")
#     i+=1

# # numbers=[50,40,23,70,56,12,5,10,7]
# # i=0
# # max=0
# for i in range(len(numbers)):
#     if numbers[i]>max:
#         max=numbers[i]
# print(max)    

# numbers=[50,40,23,70,56,12,5,10,7]
# i=0
# max=0
# while i<len(numbers):

# numbers=[50,40,23,70,56,12,5,10,7]
# i=0
# max=0
# for i in range(len(numbers)):
#     if numbers[i]>max:
#         max=numbers[i]
# print(max)    



# ab="12hours"
# a=ab*ab
# print(a)