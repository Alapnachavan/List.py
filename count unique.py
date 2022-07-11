# Count unique values inside a list.
# input_list =  [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 #because [1,2,5,8,4] are unique values.


list=[[1, 2, 2, 5, 8, 4, 4, 8]]
count=0
for ele in list:
    if(ele not in  list):
        count+=1
    list.append(ele)
print("cont of unique value are:",count)