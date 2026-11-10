d1={}
d2={}

n=int(input("Enter number of elements in dictionary 1: "))

for i in range(n):
    key=input("ENter key : ")
    value=input("ENter value")
    d1[key]=value

m=int(input("Enter number of elements of dictionary 2 : "))

for i in range(m):
    key=input("ENter key: ")
    value=input("enter value :")
    d2[key]=value

d1.update(d2)

print("Merged dictioanry : ",d1)
