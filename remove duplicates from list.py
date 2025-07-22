# ● Remove Duplicates from an Array 
# Problem: Write a function to remove duplicate values from an array. 

num=list(map(int,input("enter numbers:").split()))
list=[]
for i in num:
    if i not in list:
        list.append(i)
print(list)
