name=input("enter str: ")
vowels="aeiouAEIOU"
result=""
result2=""
for char in name:
    if char in vowels:
        result+=char
for char in result:
    if char not in result2:
        result2+=char
print(result)
print(result2)
