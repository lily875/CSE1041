x_1=int(input("x_1"))
x_2=int(input("x_2"))
x_3=int(input("x_3"))
y_1=int(input("y_1"))
y_2=int(input("y_2"))
y_3=int(input("y_3"))
area=1/2*abs(x_1*(y_2-y_3)+x_2*(y_1-y_3)+x_3*(y_1-y_2))
if area==0:
    print("these coordinates are colinear")
else :
    print("these coordinates are not colinear")
