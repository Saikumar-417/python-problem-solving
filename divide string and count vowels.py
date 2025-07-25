 Write a program that takes a string, string should be of even length. Divide the string into two equals parts, check the number of vowels in both the parts of the string. If both parts of string have same number of vowels then return true otherwise return fals.

name=input("enter name: ")
count_1=0
count_2=0
vowels="aeiouAEIOU"
if len(name)%2!=0:
    print("enter even string")

else:
    a=len(name)//2
    first=name[:a]
    second=name[a:]
    for char in first:
        if char in vowels:
          count_1+=1
    for char in second:
        if char in vowels:
          count_2+=1
    if count_1==count_2:
         print("True")
    else:
         print("False")
