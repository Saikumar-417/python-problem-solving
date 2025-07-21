# • Write a program to print the string after removing the duplicate characters  in the string.  
str=input("enter name: ")
result=""
for char in str:
    if char not in result:
        result+=char
print(result)
