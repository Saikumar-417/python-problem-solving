#  Find the Largest Element in an Array 
# Problem: Write a function to return the largest number in an array. 


list=[3,1,11,4,1,5]
r=0
for i in list:
    if r<i:
        r=i
print(r)
