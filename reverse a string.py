#reverse a string
name=input("enter name:")
res=""
for x in range(len(name)-1,-1,-1):
    res+=name[x]
print(res)
