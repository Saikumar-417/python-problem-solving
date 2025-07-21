# • Write a program to print all the Upper case letters in the string in reverse  order and then followed by the lower case letters .  
str=input("enter name :")
result=""
result2=""
for char in str:
    if char.isupper():
        result+=char
    else:
        result2+=char
result3=result[::-1]
total_result=result3+result2
print(total_result)
