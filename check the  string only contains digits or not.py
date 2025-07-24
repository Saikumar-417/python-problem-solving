# Check if String Contains Only Digits .The string "12345" consists only of digits, so the result is true.

a=input("enter: ")
b=""
for i in a:
    if i.isdigit():
        b+=i
if a==b:
    print("true")
else:
    print("false")
