# kbc koin banega caroadpati:-
# from typing import Coroutine

# print("welcome to kon banega caroadpati ") 
# question_list = [
#     "How many continents are there?",              
#     "What is the capital of India?",            
#     "NG mei kaun se course padhaya jaata hai?"  
# ]
# options_list = [
    
#     ["Four", "Nine", "Seven", "Eight"],
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]
# solution_list=[3,4,5,1]
# answer_list=["3.seven,4.delhi,1.software engineering"]
# i=0
# a=1
# y=0
# count=0
# while i<len(question_list):
#     i1=question_list[i]
#     print(i1)
#     j=0
#     while j<len(options_list[i]):
# #         print(options_list[i][j])

#         j+=1
#     i+=1
# lifeline1=input("do you want 5050 lifeline:  ")
# if lifeline1=="yes":
#     if count==0:
#         print(answer_list[y+i])
#         print(answer_list[y+a])
#         n=int(input("enter the answer:- "))
#         if n==solution_list[i]:
#             print("enter your first answer is right")
#             if n==solution_list[i]: 
#                 print("your first answer is right")
#                 print("your score is",1)
#             else:
#                 print("your first ans is wrong")
#                 print("your score is",0)
#                 print("game is over")
#             #     break
#                   count



print("welcome to kbc")
question_list=["how many containents in there ?",
"what is the capital of india?",
"navgurukul mai kaun sa course padhaya jata hai?"
]
option_list=[["four","nine","seven","eight"],
["chandigad","bhopal","chennai","delhi"],
["software engineering","counseling","tourism","agriculture"]
]
solution_list=[3,4,1]
ans=["3.seven","4.delhi","1.software engineering"]
i=0
r=1
y=0
count=0
while i<len(question_list):
    i1=(question_list)[i]
    print(i1)
    j=0
    k=i
    while j<len(option_list[i]):
        l=(option_list)[k][j]
        print(j+1,l)
        j=j+1
    lifeline1=input("do you want lifeline ? ")
    if lifeline1=="yes":
        if count==0:
            print(ans[y+i])
            print(ans[y+r])
            n=int(input("enter the answer : "))
            if n==solution_list[i]:
                print(n,"your first answer is right ")
                print(n,"your ruppes is",20000)
            else:
                    print("your first answer is wrong ")
                    print("your rupees is",0)
                    print("game is over")
                    break
            count=count+1
        else:
                print("you are already use lifeline ")
                m=int(input("enter your answer : "))
                if m==solution_list[i]:

                    print(m,"your second answer is right")
                    print(m,"your rupees is",30000)
                else:
                    print("your second answer is wrong ")
                    print("your rupees is ",0)
    elif lifeline1=="no":
            u=int(input("enter your answer "))
            if u==solution_list[i]:
                print(u,"your answer is correct ")
                print(u,"your rupees is",10000)
                print(u,"you are winner in this game")
            else:
                print("your answer is wrong")
                print("your rupees is",0)
                print("game is over")
                break
    else:
            print("error")
    i=i+1 


    