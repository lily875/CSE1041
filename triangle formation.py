side_1=int(input("a"))
side_2=int(input("b"))
side_3=int(input("c"))
if side_1+side_2>side_3:
    if side_2+side_3>side_1:
        if side_1+side_3>side_2:
            print("this can form triangle")
else :
    print("this can not form triangle")
