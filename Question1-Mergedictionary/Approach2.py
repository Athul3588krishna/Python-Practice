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