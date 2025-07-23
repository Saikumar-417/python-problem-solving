#sum of even numbers
list1=list(map(int,input("enter numbers:").split()))
sum=0
for x in list1:
    if x%2==0:
        sum+=x
print(sum)
