#check palindrome
name=input("enter name:")
res=""
for x in range(len(name)-1,-1,-1):
    res+=name[x]
if name==res:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
