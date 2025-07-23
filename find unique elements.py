# ● Find Unique Elements 
# Problem: Write a function to find the unique elements in an array  (elements that appear only once). 


list1=list(map(int,input("enter numbers:").split()))
unique_elements=[]
for item in list1:
    if list1.count(item)==1:
        unique_elements.append(item)
print(unique_elements)
