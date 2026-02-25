no=int(input("number "))
temp=no
sum=0
while(temp!=0):
    remainder=temp%10
    sum=sum+remainder
    temp=temp//10
print(f"sum is {sum}")
