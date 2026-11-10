list1=eval(input("enter list1 : "))
list2=eval(input("enter list2: "))
flag=False
for i in list1:
    if i in list2:
        flag=True
        break

print(flag)