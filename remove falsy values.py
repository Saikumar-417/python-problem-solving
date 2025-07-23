# ● Remove Falsy Values 
# Problem: Write a function that removes all falsy values from an array.  Falsy values include false, 0, "", null, undefined, and NaN. 
list1=[0,1,False,True,"",3]
new_list=[]
for item in list1:
    if item:
        new_list.append(item)
print(new_list)
