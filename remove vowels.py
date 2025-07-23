# remove vowels
name=input("enter name:")
vowels="aeiouAEIOU"
res=""
for x in name:
    if x not in vowels:
        res+=x
print(res)
