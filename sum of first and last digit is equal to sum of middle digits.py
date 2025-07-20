num=input("enter number:")
sum_1=0
sum_2=0
l=len(num)
for digit in num:
    
    if digit==num[0] or digit==num[l-1]:
         sum_1+=int(digit)
    else:
        sum_2+=int(digit)
print(sum_1)
print(sum_2)
if sum_1 == sum_2:
    print("equal")
else:
    print("not equal")
