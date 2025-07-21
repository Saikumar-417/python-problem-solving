# • Write a program to print the vowels in the given string in reverse order.
name=input("enter str:")
vowels="aeiouAEIOU"
result=""
for char in name:
    if char in vowels:
        result+=char
order=result[::-1]    
print(order)
