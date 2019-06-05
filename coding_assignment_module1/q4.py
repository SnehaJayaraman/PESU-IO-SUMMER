n=int(input("Enter an integer:"))
k=n
sum=0
while k>0:
    t=k%10;
    sum=sum+t
    k=k//10
print("The sum of digits of the integer",n,"is",sum)
