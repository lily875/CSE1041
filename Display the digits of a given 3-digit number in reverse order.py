no=int(input("number "))
reverse=0
temp=no
while (temp!=0):
    remainder=temp%10
    reverse=(reverse*10)+remainder
    temp=temp//10
print(f"{reverse} is the reversed no")
