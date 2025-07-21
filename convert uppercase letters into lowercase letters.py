# Write a program to convert all the upper case letters in the given string to  lower case letter and vice versa.  
str=input("enter number: ")
result=""
for char in str:
    if char.isupper():
        result+=char.lower()
    else:
        result+=char.upper()
print(result)
