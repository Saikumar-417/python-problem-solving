#vowels count
name=input("enter name:")
vowels="aeiouAEIOU"
count=0
for x in name:
    if x  in vowels:
        count+=1
print(count)
