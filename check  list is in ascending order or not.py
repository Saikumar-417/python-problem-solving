# ● Check if Array is Sorted 
# Problem: Write a function to check if an array is sorted in ascending  order.  
. 
num=list(map(int,input("enter numbers:").split()))

print(num)
if num == sorted(num):
    print("true")
else:
    print("false")
