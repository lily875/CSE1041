# You are using Python
elements= input()
my_list= list(map(int,elements.split()))
print(f"list: {my_list}")
if len(my_list)!=len(set(my_list)):
    print("list contains duplicate elements")
else:
    print("All elements are unique")
