list1=eval(input("enter list1 : "))
list2=eval(input("enter list2: "))
flag=False
for i in list1:
    if i in list2:
        flag=True
        break

print(flag)


### Algorithm – Check Common Elements in Two Lists

1. Start.
2. Read two lists from the user.
3. Initialize `flag = False`.
4. Traverse each element in the first list.
5. Check whether the element is present in the second list.
6. If a common element is found, set `flag = True` and terminate the loop.
7. Display the value of `flag`.
8. Stop.
