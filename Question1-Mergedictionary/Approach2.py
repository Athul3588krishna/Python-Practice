d1={}
d2={}
n=int(input("Enter dictionary 1 elements : "))

for i in range(n):
    key=input("ENter key : ")
    value=input("Enter value: ")
    d1[key]=value

m=int(input("Enter dictionary 2 elements : "))

for i in range(m):
    key=input("Enter key : ")
    value=input("Enter value: ")
    d1[key]=value

d1.update(d2)

print("Merged dictionary : ",d1)


### Algorithm – Merge Two Dictionaries

1. Start.
2. Initialize two empty dictionaries.
3. Read the number of elements in the first dictionary.
4. Read keys and values and store them in the first dictionary.
5. Read the number of elements in the second dictionary.
6. Read keys and values and store them in the second dictionary.
7. Merge the second dictionary into the first dictionary using `update()`.
8. Display the merged dictionary.
9. Stop.

