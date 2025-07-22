#Problem: Write a function to reverse the elements in an array. 

num=list(map(int,input("enter numbers:").split()))
new=[]
for i in range(len(num)-1,-1,-1):
    new.append(num[i])
print(new)
