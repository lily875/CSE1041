# You are using Python
num=int(input())
i=1
while(i<=num):
    if (i%2!=0):
        if i+2>num:
            print(f"{i}")
        else:
            print(f"{i},",end="")
            
        i=i+1
    else:
        i=i+1
    
