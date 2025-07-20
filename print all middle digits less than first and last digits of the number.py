num=input("enter number:")
l=len(num)-1
for digit in num:
  if digit == num[0] or digit == num[l]:
      print()
       
  else:
       if digit < num[0] and num[l]:
           print("true ")
           break
       else:
           print("false")
