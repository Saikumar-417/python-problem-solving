num=input("enter number:")
revstr=""
for i in range(len(num)-1,-1,-1):
    revstr+=num[i]
print(revstr)
