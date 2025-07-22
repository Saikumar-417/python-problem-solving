# ● Sum of All Elements 
# Problem: Write a function that returns the sum of all elements in an array. 


num=list(map(int, input("Enter numbers separated by space: ").split()))
print(num)
count=0
for i in num:
    count+=i
print(count)
