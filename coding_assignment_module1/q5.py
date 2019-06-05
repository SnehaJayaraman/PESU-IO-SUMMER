
#Method-1:Using built-in function
str=input("Enter a string:")
if str.isnumeric():
    print("The string entered",str,"is numeric")
else:
   print("The string entered",str,"is not numeric")
    
#Method-2
str=input("Enter a string:")
i=0
for ch in str:
    if(ord(ch)>=48 and ord(ch)<=57):
        i=i+1
    else:
        break
if i==len(str):
    print("The entered string",str,"is numeric")
else:
    print("The entered string",str,"is not numeric")
