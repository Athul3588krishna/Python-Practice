filename=input("Enter the name of file : ")
f=open(filename,"r")
lines=f.readlines()
print("The number of lines : ",len(lines))
