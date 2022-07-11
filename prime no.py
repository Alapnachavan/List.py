#list=[1,2,3,4,5,6,7,8,9,11,12,13,14]
prime_num=[]
i=0
list=[]
while i<len(list):
    list_elements=list[i]
    count=0
    j=1
    while list_elements>=j:
        if list_elements%j==0:
            count+=1
        j=j+1
    if count==2:
        prime_num.append(list_elements)
    i+=1
print(prime_num)
