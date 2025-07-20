a=input("enter:")
b=len(a)
mid=b//2
result=""
for i in range(b):
    if b%2==0:
        if i==mid or i==mid-1:
            result+=a[i]
    else:
        if i==mid:
            result+=a[i]
print(result)
